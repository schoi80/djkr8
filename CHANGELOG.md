# CHANGELOG

<!-- version list -->

## v1.5.0 (2026-01-17)

### Bug Fixes

- Resolve pre-commit linting issues
  ([`74904f2`](https://github.com/schoi80/djkr8/commit/74904f2ec7634b12d9e932e1804b47b17e122809))

### Documentation

- Updated project detail
  ([`0c7026c`](https://github.com/schoi80/djkr8/commit/0c7026c5a7410b5791e02775c24d7dd810ba3bec))

### Features

- Add harmonic mixing philosophies from Mixed In Key
  ([`4c78565`](https://github.com/schoi80/djkr8/commit/4c78565fbbaf44bfc7bde1cb8e16b86bf0a4c035))

- Add max +1 energy increase constraint when flow is enforced
  ([`47924bb`](https://github.com/schoi80/djkr8/commit/47924bbf2f2c29eb6eb6caa429a0a2cd99ca1b4a))


## v1.4.0 (2026-01-16)

### Features

- Rebranding to djkr8
  ([`1788fcd`](https://github.com/schoi80/dj-krate/commit/1788fcd6c94114eb497222b85d8d4d5b22f55d76))


## v1.3.0 (2026-01-16)

### Chores

- Renamed to djkr8
  ([`158a8a6`](https://github.com/schoi80/djkr8/commit/158a8a63fcc952865724fd7ca8030aee73e82a12))

### Features

- Rebranded to djkr8
  ([`4774480`](https://github.com/schoi80/djkr8/commit/47744803ccf3a06fbe9b1fc0c762cdac75ed8953))


## v1.2.0 (2026-01-16)

### Features

- Enforce energy range (1-5) and non-decreasing flow constraint
  ([`3346e7b`](https://github.com/schoi80/dj-playlist-optimizer/commit/3346e7b45166c098d10bbcf2b31dd5e1a62a9fe6))

- Make energy flow constraint togglable and update documentation
  ([`a1a9f5b`](https://github.com/schoi80/dj-playlist-optimizer/commit/a1a9f5b3b1d135f7a1f6af571ef10b94c7e87521))


## v1.1.0 (2026-01-16)

### Documentation

- Add new `AGENTS.md` files to `src` and `tests` directories and refactor the main `AGENTS.md` with
  updated project details.
  ([`87314cb`](https://github.com/schoi80/djkr8/commit/87314cb21da8ed4b9f14b0db08a062cd250cb09a))

### Features

- Add comprehensive test suite for Rekordbox integration, CLI, models, and optimizer features, and
  configure pytest-cov for coverage reporting.
  ([`2df81c5`](https://github.com/schoi80/djkr8/commit/2df81c58e9802cec72ffa1fa89eb4c1c3767f043))

- Add Rekordbox database integration for loading playlists and tracks via new CLI options.
  ([`0e3db17`](https://github.com/schoi80/djkr8/commit/0e3db17259deb0b8b8479dfb56037f289cf1e512))

- Introduce Rekordbox XML export and direct database integration for optimized playlists, including
  track metadata enrichment.
  ([`efcb547`](https://github.com/schoi80/djkr8/commit/efcb5474e8bd80917ddd0a6123bf8bd71f94b531))

### Testing

- Improve robustness of Rekordbox XML parsing assertions and adapt database mock to keyword
  arguments.
  ([`cfd9541`](https://github.com/schoi80/djkr8/commit/cfd95419b30da0e3717af6a03fc90470d8a64389))


## v1.0.0 (2026-01-16)

- Initial Release
