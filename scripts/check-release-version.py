"""Validate release artifacts without importing or executing packaged code."""

import re
import ast
import sys
import json
import tarfile
import zipfile
from pathlib import Path
from email.parser import BytesParser


def check_release(root: Path, tag: str) -> None:
    if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", tag):
        raise ValueError("Publishing requires an explicit stable release tag (vX.Y.Z), not a branch")
    expected = tag[1:]
    versions = {"release manifest": json.loads((root / ".release-please-manifest.json").read_text())["."]}
    module = ast.parse((root / "src/businessradar/_version.py").read_text())
    assignments = [
        node
        for node in module.body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "__version__" for target in node.targets)
    ]
    if len(assignments) != 1:
        raise ValueError("Expected exactly one literal __version__ assignment")
    versions["runtime version"] = ast.literal_eval(assignments[0].value)
    wheels = list((root / "dist").glob("*.whl"))
    sdists = list((root / "dist").glob("*.tar.gz"))
    if (
        len(wheels) != 1
        or len(sdists) != 1
        or len([path for path in (root / "dist").iterdir() if path.name != ".gitignore"]) != 2
    ):
        raise ValueError("Expected exactly one wheel and one source distribution")
    with zipfile.ZipFile(wheels[0]) as wheel:
        names = [name for name in wheel.namelist() if name.endswith(".dist-info/METADATA")]
        if len(names) != 1:
            raise ValueError("Expected exactly one wheel METADATA file")
        wheel_metadata = BytesParser().parsebytes(wheel.read(names[0]))
    with tarfile.open(sdists[0]) as sdist:
        members = [
            member for member in sdist.getmembers() if member.name.count("/") == 1 and member.name.endswith("/PKG-INFO")
        ]
        if len(members) != 1 or not members[0].isfile():
            raise ValueError("Expected exactly one top-level source PKG-INFO file")
        stream = sdist.extractfile(members[0])
        if stream is None:
            raise ValueError("Source metadata is unreadable")
        with stream:
            sdist_metadata = BytesParser().parsebytes(stream.read())
    for label, metadata in [("wheel", wheel_metadata), ("source distribution", sdist_metadata)]:
        if metadata.get_all("Name") != ["businessradar"] or len(metadata.get_all("Version", [])) != 1:
            raise ValueError(f"Invalid {label} package metadata")
        versions[label] = metadata["Version"]
    for label, version in versions.items():
        if version != expected:
            raise ValueError(f"{label} version {version!r} does not match release {tag}; refusing to publish")
    if (
        wheels[0].name != f"businessradar-{expected}-py3-none-any.whl"
        or sdists[0].name != f"businessradar-{expected}.tar.gz"
    ):
        raise ValueError("Artifact filenames do not match the release version")
    print(f"Verified {tag}: manifest, runtime, wheel and source distribution agree")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python scripts/check-release-version.py vX.Y.Z")
        check_release(Path(__file__).resolve().parent.parent, sys.argv[1])
    except (ValueError, OSError, KeyError, SyntaxError, tarfile.TarError, zipfile.BadZipFile) as exc:
        print(f"Release validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
