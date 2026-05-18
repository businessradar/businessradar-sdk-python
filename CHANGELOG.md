# Changelog

## 1.18.0 (2026-05-18)

Full Changelog: [v1.17.0...v1.18.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.17.0...v1.18.0)

### Features

* **api:** api update ([dc562ba](https://github.com/businessradar/businessradar-sdk-python/commit/dc562ba99f33ccbe71a440d131a2a3086aae65d6))
* **api:** api update ([918a0d0](https://github.com/businessradar/businessradar-sdk-python/commit/918a0d04e112f8b3a949692d06dbc3d34f6837ec))
* **api:** api update ([8f87bac](https://github.com/businessradar/businessradar-sdk-python/commit/8f87bacbfe86c51b2f14bd34cff70a5ecf3ac634))
* **api:** manual updates ([84dcea3](https://github.com/businessradar/businessradar-sdk-python/commit/84dcea38f025af11b50e7485d2d4c5a35547fbfc))
* **api:** manual updates ([fe46207](https://github.com/businessradar/businessradar-sdk-python/commit/fe46207954171e430d5a26839a2dc3035d3ae0a9))
* **internal/types:** support eagerly validating pydantic iterators ([4b3fa02](https://github.com/businessradar/businessradar-sdk-python/commit/4b3fa02e36136a8614cf5532837bf5732a943b52))
* support setting headers via env ([1d911cd](https://github.com/businessradar/businessradar-sdk-python/commit/1d911cd2eddcb399129192a0c9868725d23a1f46))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([6e5dd10](https://github.com/businessradar/businessradar-sdk-python/commit/6e5dd106cb90297c23f55c190ee72d626a9ba12b))
* **client:** preserve hardcoded query params when merging with user params ([299adce](https://github.com/businessradar/businessradar-sdk-python/commit/299adcec4e31289969de227b77ef93b42fd31e64))
* ensure file data are only sent as 1 parameter ([46712c6](https://github.com/businessradar/businessradar-sdk-python/commit/46712c68db2d1e89da0669d920153d77303b9d5d))
* use correct field name format for multipart file arrays ([274ed7e](https://github.com/businessradar/businessradar-sdk-python/commit/274ed7ef77399da9c999ddd2664f549e24c744ef))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([d3d5788](https://github.com/businessradar/businessradar-sdk-python/commit/d3d578838c682539f86ec9e750fd465bdc1f77d0))


### Chores

* **internal:** more robust bootstrap script ([95c2e2e](https://github.com/businessradar/businessradar-sdk-python/commit/95c2e2ef9db387056828060e155275a6b3a6386a))
* **internal:** reformat pyproject.toml ([6f3d95d](https://github.com/businessradar/businessradar-sdk-python/commit/6f3d95dc27218506536089054ef127d3a54fc0ad))

## 1.17.0 (2026-04-02)

Full Changelog: [v1.16.0...v1.17.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.16.0...v1.17.0)

### Features

* **api:** manual updates ([3a63603](https://github.com/businessradar/businessradar-sdk-python/commit/3a63603c59e0076df0093b131dd13ecbaf9e2443))

## 1.16.0 (2026-04-02)

Full Changelog: [v1.15.0...v1.16.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.15.0...v1.16.0)

### Features

* **api:** api update ([9fec827](https://github.com/businessradar/businessradar-sdk-python/commit/9fec82723fdd823822b93b4a9309a9897456441e))

## 1.15.0 (2026-03-30)

Full Changelog: [v1.14.0...v1.15.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.14.0...v1.15.0)

### Features

* **api:** api update ([a09bb90](https://github.com/businessradar/businessradar-sdk-python/commit/a09bb90c9c1bd1fe79c34768acff3d31d2b9a14f))
* **api:** api update ([5247987](https://github.com/businessradar/businessradar-sdk-python/commit/52479872db8067a5f47c7e14bbd34a3c5e566070))
* **api:** api update ([8d3e4c7](https://github.com/businessradar/businessradar-sdk-python/commit/8d3e4c7fdb7c94851db2018aaf21fef5849e6d66))
* **api:** manual updates ([80489da](https://github.com/businessradar/businessradar-sdk-python/commit/80489da22ed156b46cf8741f3292d6f77b3be2d0))
* **internal:** implement indices array format for query and form serialization ([2bb17a7](https://github.com/businessradar/businessradar-sdk-python/commit/2bb17a71139462ba29536ac73bbd81828fbeb4cb))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([1852b69](https://github.com/businessradar/businessradar-sdk-python/commit/1852b69eec6d104b6b452d1406d6dced1069d996))
* **pydantic:** do not pass `by_alias` unless set ([cf0901d](https://github.com/businessradar/businessradar-sdk-python/commit/cf0901d915c2982071acd0b354ee110904039b27))
* sanitize endpoint path params ([7a2f124](https://github.com/businessradar/businessradar-sdk-python/commit/7a2f12444661e14b8d2d6f3a933c9d4d75fccc3d))


### Chores

* **ci:** skip lint on metadata-only changes ([70249e1](https://github.com/businessradar/businessradar-sdk-python/commit/70249e1f18ee11f24ea1a499be96c2f0c155fefd))
* **internal:** tweak CI branches ([5e2e210](https://github.com/businessradar/businessradar-sdk-python/commit/5e2e21092a41a8f18b7ffe4d6552fa2471567798))
* **internal:** update gitignore ([5bc45eb](https://github.com/businessradar/businessradar-sdk-python/commit/5bc45eb7f42d60657c446991f405df279e46d804))

## 1.14.0 (2026-03-13)

Full Changelog: [v1.13.0...v1.14.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.13.0...v1.14.0)

### Features

* **api:** api update ([d836225](https://github.com/businessradar/businessradar-sdk-python/commit/d8362252e8321b49a70652c5ca4c54842590801e))

## 1.13.0 (2026-03-12)

Full Changelog: [v1.12.1...v1.13.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.12.1...v1.13.0)

### Features

* **api:** api update ([d8ba8c4](https://github.com/businessradar/businessradar-sdk-python/commit/d8ba8c48944674ef288d78ea875fd01c87a9dc61))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([1d33cb3](https://github.com/businessradar/businessradar-sdk-python/commit/1d33cb3f8e6e6308b8c08e0372248e78a47f8cfe))

## 1.12.1 (2026-02-27)

Full Changelog: [v1.12.0...v1.12.1](https://github.com/businessradar/businessradar-sdk-python/compare/v1.12.0...v1.12.1)

## 1.12.0 (2026-02-27)

Full Changelog: [v1.11.0...v1.12.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.11.0...v1.12.0)

### Features

* **api:** api update ([4ec7c18](https://github.com/businessradar/businessradar-sdk-python/commit/4ec7c18bde49a9de8054aa780bbcc3b124c2cee0))


### Chores

* format all `api.md` files ([29c800c](https://github.com/businessradar/businessradar-sdk-python/commit/29c800cd9edaf98f60852af4591f71a1ec65db4b))
* **internal:** add request options to SSE classes ([6d25dce](https://github.com/businessradar/businessradar-sdk-python/commit/6d25dceb335b94a638d78775aff9921eec5646bf))
* **internal:** bump dependencies ([85d6078](https://github.com/businessradar/businessradar-sdk-python/commit/85d6078a3651504b08a40f5fd6190cb0e187a399))
* **internal:** fix lint error on Python 3.14 ([ced88c4](https://github.com/businessradar/businessradar-sdk-python/commit/ced88c49da08bf4abbdf280f8b1b0aaaaa0884d4))
* **internal:** make `test_proxy_environment_variables` more resilient ([53edf3b](https://github.com/businessradar/businessradar-sdk-python/commit/53edf3b574ccd93ba9e86dddb9c3b29f60f13036))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([fb33a8c](https://github.com/businessradar/businessradar-sdk-python/commit/fb33a8c4a98ffe0a706af1b1b9a06bff5b20086a))
* **internal:** remove mock server code ([a897eb3](https://github.com/businessradar/businessradar-sdk-python/commit/a897eb3a518a0f8a4c5309148d419c363af366fc))
* update mock server docs ([0283a7d](https://github.com/businessradar/businessradar-sdk-python/commit/0283a7df9cb60a34b611066b781cdb4a43d293a9))

## 1.11.0 (2026-01-30)

Full Changelog: [v1.10.0...v1.11.0](https://github.com/businessradar/businessradar-sdk-python/compare/v1.10.0...v1.11.0)

### Features

* **api:** api update ([751609e](https://github.com/businessradar/businessradar-sdk-python/commit/751609e9a91c3137235d351e8f2078e4dc286212))
* **api:** api update ([ad589c1](https://github.com/businessradar/businessradar-sdk-python/commit/ad589c1f3e211c6703a5ef0dba5475829b7cbfc6))
* **api:** api update ([fb8d21d](https://github.com/businessradar/businessradar-sdk-python/commit/fb8d21d82b2b08a384f92d9b42bacdd7b1a47939))
* **api:** api update ([b3bd594](https://github.com/businessradar/businessradar-sdk-python/commit/b3bd5945e8823db72e7fcdc4250a3b14c8bb090f))
* **api:** api update ([180ec4a](https://github.com/businessradar/businessradar-sdk-python/commit/180ec4a2ef2f87446f0cc1cbe072492984692992))
* **api:** api update ([351a8b8](https://github.com/businessradar/businessradar-sdk-python/commit/351a8b81480156274f0d525aa3e611ae2db0c4cb))
* **api:** api update ([97abde8](https://github.com/businessradar/businessradar-sdk-python/commit/97abde8d2428d6bbd9d8ebfc650e519533a06c87))
* **api:** manual updates ([ac7a60f](https://github.com/businessradar/businessradar-sdk-python/commit/ac7a60f05af09c73e3ca85f6cd01ad38cfa437fb))

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
