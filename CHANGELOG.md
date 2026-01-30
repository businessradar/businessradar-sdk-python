# Changelog

## 1.10.0 (2026-01-30)

Full Changelog: [v1.9.0...v1.10.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.9.0...v1.10.0)

### Features

* **api:** api update ([65cea5a](https://github.com/businessradar/businessradar-sdk-python/commit/65cea5afd440b39beb56785302b6533fc429dcdb))
* **api:** api update ([6ffdd96](https://github.com/businessradar/businessradar-sdk-python/commit/6ffdd96ce8eb8c7a0efaf82434d830026237dcb7))
* **api:** manual updates ([a83b442](https://github.com/businessradar/businessradar-sdk-python/commit/a83b442411d77178308652b005dd33ee3f9a12b5))
* **client:** add custom JSON encoder for extended type support ([ebb8af7](https://github.com/businessradar/businessradar-sdk-python/commit/ebb8af7e242b1b25d4531840e290306965f66e01))

## 1.9.0 (2026-01-29)

Full Changelog: [v1.8.0...v1.9.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.8.0...v1.9.0)

### Features

* **api:** api update ([82cec3b](https://github.com/businessradar/businessradar-sdk-python/commit/82cec3b3d774401a19b36f50f2643a5e49162efa))
* **api:** manual updates ([7738a48](https://github.com/businessradar/businessradar-sdk-python/commit/7738a48749ddfec3b415faeed9b3076366af8e80))


### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([fd6867a](https://github.com/businessradar/businessradar-sdk-python/commit/fd6867a449341aff6b9a66f4d01028b9caba9f33))


### Chores

* configure new SDK language ([825093b](https://github.com/businessradar/businessradar-sdk-python/commit/825093b3acc68b935de9a74856a9ab947ebe564e))
* update SDK settings ([91b4db2](https://github.com/businessradar/businessradar-sdk-python/commit/91b4db2ea1d96919a478bbd09a1d42197f7d7c63))

## 1.8.0 (2026-01-27)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.7.0...v1.8.0)

### Features

* **api:** api update ([35bb2a2](https://github.com/businessradar/businessradar-sdk-python/commit/35bb2a2b8c4e474dd14bd0506d4a67b1cbe27069))

## 1.7.0 (2026-01-26)

Full Changelog: [v1.6.0...v1.7.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.6.0...v1.7.0)

### Features

* **api:** api update ([12ef8ee](https://github.com/businessradar/businessradar-sdk-python/commit/12ef8ee497a0559229fc894c2f0535187dd53358))
* **api:** manual updates ([804f1dc](https://github.com/businessradar/businessradar-sdk-python/commit/804f1dc34e67d001d49e117924f615b1a6dde22b))
* **client:** add support for binary request streaming ([eaf59bb](https://github.com/businessradar/businessradar-sdk-python/commit/eaf59bbf6a6abaa8bfec34d28390df64e6eeeab6))


### Bug Fixes

* use async_to_httpx_files in patch method ([5fd2ea4](https://github.com/businessradar/businessradar-sdk-python/commit/5fd2ea455cc9d37831f24357acc442f0909ddf07))


### Chores

* **ci:** upgrade `actions/github-script` ([067b9dd](https://github.com/businessradar/businessradar-sdk-python/commit/067b9dde0cf6ab544c1e032f4598183469e11000))
* **internal:** add `--fix` argument to lint script ([0c7ee4e](https://github.com/businessradar/businessradar-sdk-python/commit/0c7ee4eae333d5f94b69daaf310f12b78c707fae))
* **internal:** add missing files argument to base client ([186d8bf](https://github.com/businessradar/businessradar-sdk-python/commit/186d8bfc249d33bf43f0c659c748373b2d482ed0))
* **internal:** codegen related update ([31f3fe5](https://github.com/businessradar/businessradar-sdk-python/commit/31f3fe50d96c12590f3edacf7526b8a4af3cfd45))
* **internal:** update `actions/checkout` version ([d72d132](https://github.com/businessradar/businessradar-sdk-python/commit/d72d1328c7818e894acfecbdb514ac8f63239bc3))
* speedup initial import ([8043b1f](https://github.com/businessradar/businessradar-sdk-python/commit/8043b1f060383318e0e7c85806e6bd9fe66b221a))

## 1.6.0 (2025-12-15)

Full Changelog: [v1.5.1...v1.6.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.5.1...v1.6.0)

### Features

* **api:** api update ([10044f7](https://github.com/businessradar/businessradar-sdk-python/commit/10044f76ebe043321dd17ace090b9bebf3ea237a))
* **api:** api update ([79c8f34](https://github.com/businessradar/businessradar-sdk-python/commit/79c8f34ca6f2f88b6854ac846c89ec8efff455ab))


### Bug Fixes

* compat with Python 3.14 ([791d295](https://github.com/businessradar/businessradar-sdk-python/commit/791d2952d47bae569018154e810807b49a268ffb))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([bac5787](https://github.com/businessradar/businessradar-sdk-python/commit/bac5787696bafd43a0e5fda396c26f147cd41e57))
* ensure streams are always closed ([d40fa9d](https://github.com/businessradar/businessradar-sdk-python/commit/d40fa9d5659d7c8401b199451cc125450e02c2e3))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([08baa95](https://github.com/businessradar/businessradar-sdk-python/commit/08baa95b47f8926140296afbc6f266409ab977d3))


### Chores

* add missing docstrings ([9112e6c](https://github.com/businessradar/businessradar-sdk-python/commit/9112e6cb061f8f537980e06b3859615306033346))
* add Python 3.14 classifier and testing ([08e7bb8](https://github.com/businessradar/businessradar-sdk-python/commit/08e7bb8c02a52c07014d3cbcde6c7ac7cbee59ed))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([864efbf](https://github.com/businessradar/businessradar-sdk-python/commit/864efbf05d8a2734050fef58e9a23856ddb75784))
* **docs:** use environment variables for authentication in code snippets ([f20e275](https://github.com/businessradar/businessradar-sdk-python/commit/f20e2751a9b0f091191e2139ecf61bffa8f9f82f))
* **internal:** grammar fix (it's -&gt; its) ([76d2d86](https://github.com/businessradar/businessradar-sdk-python/commit/76d2d86f6764f50a4df3fcad2e5e13f3fcae6913))
* **package:** drop Python 3.8 support ([2c423b3](https://github.com/businessradar/businessradar-sdk-python/commit/2c423b3eb354cc820966cc462ecef04643ed9b22))
* update lockfile ([821f301](https://github.com/businessradar/businessradar-sdk-python/commit/821f301afb14b25f5d0d5c4055b19ecff9b0f0c4))

## 1.5.1 (2025-10-31)

Full Changelog: [v1.4.2...v1.5.1](https://github.com/businessradar/businessradar-sdk-python/compare/v1.4.2...v1.5.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([b61515d](https://github.com/businessradar/businessradar-sdk-python/commit/b61515d03bc0c230dcae28a3508cf66da165a5d0))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([3362d7a](https://github.com/businessradar/businessradar-sdk-python/commit/3362d7a0d94899b34c2d09e17df44b16f68d3c4e))

## 1.4.2 (2025-10-24)

Full Changelog: [v1.4.1...v1.4.2](https://github.com/businessradar/businessradar-sdk-python/compare/v1.4.1...v1.4.2)

### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([99414e4](https://github.com/businessradar/businessradar-sdk-python/commit/99414e4051836ed883db3868dab334e51ddce1ea))
* **internal:** detect missing future annotations with ruff ([e19b26a](https://github.com/businessradar/businessradar-sdk-python/commit/e19b26acd7fde3cfa9395d0e55615928dfaed3d2))

## 1.4.1 (2025-09-22)

Full Changelog: [v1.4.0...v1.4.1](https://github.com/businessradar/businessradar-sdk-python/compare/v1.4.0...v1.4.1)

### Chores

* sync repo ([0f74c25](https://github.com/businessradar/businessradar-sdk-python/commit/0f74c256f039ad9fd815955a0bf29dc4a5f611c4))

## 1.4.0 (2025-09-20)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.3.0...v1.4.0)

### Features

* improve future compat with pydantic v3 ([082bbe1](https://github.com/businessradar/businessradar-sdk-python/commit/082bbe1ee170a17a2d97fa98e81a147a39acc7ad))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([61c6d6b](https://github.com/businessradar/businessradar-sdk-python/commit/61c6d6bbf14bf35a09bb956ca18bc5afa3f85f42))
* **internal:** move mypy configurations to `pyproject.toml` file ([8dc8271](https://github.com/businessradar/businessradar-sdk-python/commit/8dc827195bf21031c1d7ffe1a73ecae6333aba6e))
* **internal:** update pydantic dependency ([ce274a6](https://github.com/businessradar/businessradar-sdk-python/commit/ce274a6655430552d5cbb79e7a1a028242437b0c))
* **tests:** simplify `get_platform` test ([cf21969](https://github.com/businessradar/businessradar-sdk-python/commit/cf2196994bf945079ba7fc459131721c14551dd2))
* **types:** change optional parameter type from NotGiven to Omit ([4863ae2](https://github.com/businessradar/businessradar-sdk-python/commit/4863ae26849677a6fc34fc5660364f04d4a5a1e8))

## 1.3.0 (2025-09-03)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.2.0...v1.3.0)

### Features

* **types:** replace List[str] with SequenceNotStr in params ([f0cd154](https://github.com/businessradar/businessradar-sdk-python/commit/f0cd154a08d32800ff262980b2a01ff80bff3f36))

## 1.2.0 (2025-09-02)

Full Changelog: [v1.1.1...v1.2.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.1.1...v1.2.0)

### Features

* **api:** api update ([3a8dedb](https://github.com/businessradar/businessradar-sdk-python/commit/3a8dedbc0cd81dc657b80bebf75c7072ef425d91))
* **api:** manual updates ([533ebf3](https://github.com/businessradar/businessradar-sdk-python/commit/533ebf3f5a506098c7254864a97e33f1624340e4))
* **api:** manual updates ([e18d51c](https://github.com/businessradar/businessradar-sdk-python/commit/e18d51c855d3210f3bfb914f37f6706f9cb71097))
* **api:** manual updates ([a0f0f58](https://github.com/businessradar/businessradar-sdk-python/commit/a0f0f587f70ffa601c48e9ba9fe17854c9d46303))
* **api:** manual updates ([9635b27](https://github.com/businessradar/businessradar-sdk-python/commit/9635b274694ae4afde51616e11c00bfe6ce91a2b))

## 1.1.1 (2025-09-02)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/businessradar/businessradar-sdk-python/compare/v1.1.0...v1.1.1)

## 1.1.0 (2025-09-02)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** manual updates ([40b5e21](https://github.com/businessradar/businessradar-sdk-python/commit/40b5e210578ea543112bea55cdf9181c3efff140))
* **api:** manual updates ([4c22e88](https://github.com/businessradar/businessradar-sdk-python/commit/4c22e88e12ff5739a9cfb0ac989262e4cf9ed027))

## 1.0.0 (2025-09-02)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/businessradar/businessradar-sdk-python/compare/v0.0.1...v1.0.0)

### Chores

* update SDK settings ([3f921f8](https://github.com/businessradar/businessradar-sdk-python/commit/3f921f8414edde86fd83085b013f18c9c885d62e))
* update SDK settings ([b043f36](https://github.com/businessradar/businessradar-sdk-python/commit/b043f361a379c89f5a3c18a4842e8c8cfb3d4120))
* update SDK settings ([2cb91ef](https://github.com/businessradar/businessradar-sdk-python/commit/2cb91ef1ff9154cabb9d24d2226572b8ae9d2d7c))
