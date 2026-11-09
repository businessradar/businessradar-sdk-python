"""Release validation regression tests; no network or package imports required."""

import io
import os
import json
import runpy
import shutil
import tarfile
import zipfile
import tempfile
import unittest
import subprocess
from pathlib import Path

check_release = runpy.run_path(str(Path(__file__).with_name("check-release-version.py")))["check_release"]


class ReleaseVersionTests(unittest.TestCase):
    def setUp(self) -> None:  # pyright: ignore[reportImplicitOverride]
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "src/businessradar").mkdir(parents=True)
        (self.root / "dist").mkdir()
        self.fixture()

    def fixture(self, version: str = "1.31.1", wheel_version: str = "1.31.1", sdist_version: str = "1.31.1") -> None:
        (self.root / ".release-please-manifest.json").write_text(json.dumps({".": version}))
        (self.root / "src/businessradar/_version.py").write_text(f'__version__ = "{version}"\n')
        with zipfile.ZipFile(self.root / "dist/businessradar-1.31.1-py3-none-any.whl", "w") as wheel:
            wheel.writestr(
                "businessradar-1.31.1.dist-info/METADATA", f"Name: businessradar\nVersion: {wheel_version}\n"
            )
        with tarfile.open(self.root / "dist/businessradar-1.31.1.tar.gz", "w:gz") as sdist:
            data = f"Name: businessradar\nVersion: {sdist_version}\n".encode()
            info = tarfile.TarInfo("businessradar-1.31.1/PKG-INFO")
            info.size = len(data)
            sdist.addfile(info, io.BytesIO(data))

    def test_matching_release(self) -> None:
        (self.root / "dist/.gitignore").write_text("*")
        check_release(self.root, "v1.31.1")

    def test_original_incident(self) -> None:
        self.fixture("1.30.0", "1.30.0", "1.30.0")
        with self.assertRaisesRegex(ValueError, "does not match"):
            check_release(self.root, "v1.31.0")

    def test_each_artifact_must_match(self) -> None:
        for wheel, sdist in [("1.30.0", "1.31.1"), ("1.31.1", "1.30.0")]:
            with self.subTest(wheel=wheel, sdist=sdist):
                self.fixture(wheel_version=wheel, sdist_version=sdist)
                with self.assertRaisesRegex(ValueError, "does not match"):
                    check_release(self.root, "v1.31.1")

    def test_runtime_mismatch(self) -> None:
        (self.root / "src/businessradar/_version.py").write_text('__version__ = "1.30.0"\n')
        with self.assertRaisesRegex(ValueError, "runtime version"):
            check_release(self.root, "v1.31.1")

    def test_reject_branch_or_missing_tag(self) -> None:
        for tag in ["", "main", "1.31.1", "v1.31.1\n", "v1.31.1rc1"]:
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                check_release(self.root, tag)

    def test_missing_artifact(self) -> None:
        next((self.root / "dist").glob("*.whl")).unlink()
        with self.assertRaisesRegex(ValueError, "exactly one wheel"):
            check_release(self.root, "v1.31.1")

    def test_extra_file_cannot_be_uploaded(self) -> None:
        (self.root / "dist/stale.whl").touch()
        with self.assertRaisesRegex(ValueError, "exactly one wheel"):
            check_release(self.root, "v1.31.1")

    def test_metadata_cannot_hide_behind_filename(self) -> None:
        self.fixture(wheel_version="1.30.0")
        with self.assertRaisesRegex(ValueError, "wheel version"):
            check_release(self.root, "v1.31.1")

    def test_runtime_is_never_executed(self) -> None:
        (self.root / "src/businessradar/_version.py").write_text(
            'raise RuntimeError("do not execute")\n__version__ = "1.31.1"\n'
        )
        check_release(self.root, "v1.31.1")

    def test_ambiguous_runtime_version(self) -> None:
        (self.root / "src/businessradar/_version.py").write_text('__version__ = "1.31.1"\n__version__ = "1.30.0"\n')
        with self.assertRaisesRegex(ValueError, "exactly one literal"):
            check_release(self.root, "v1.31.1")

    def test_publisher_rejects_branch_dirty_checkout_and_wrong_commit(self) -> None:
        source = Path(__file__).resolve().parent.parent
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "bin").mkdir()
            shutil.copy(source / "bin/publish-pypi", root / "bin/publish-pypi")

            def git(*args: str) -> None:
                subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)

            git("init")
            git("config", "user.email", "tests@example.invalid")
            git("config", "user.name", "Release tests")
            git("add", ".")
            git("commit", "-m", "test")
            git("tag", "v1.31.1")
            env = {**os.environ, "RELEASE_TAG": "v1.31.1", "GITHUB_ACTIONS": "true", "GITHUB_REF_TYPE": "branch"}

            def rejected(message: str) -> None:
                result = subprocess.run(["bash", "bin/publish-pypi"], cwd=root, env=env, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)

            rejected("requires a tag ref")
            env["GITHUB_REF_TYPE"] = "tag"
            (root / "dirty").touch()
            rejected("uncommitted changes")
            git("add", ".")
            git("commit", "-m", "new head")
            rejected("does not match")


if __name__ == "__main__":
    unittest.main()
