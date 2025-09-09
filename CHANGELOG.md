# Changelog

## [0.1.3](https://github.com/albertomh/django-e2e-benchmarks/compare/v0.1.2...v0.1.3) (2025-09-09)


### Bug Fixes

* **ci:** Ensure caller workflow passes secrets to django-checks job ([#18](https://github.com/albertomh/django-e2e-benchmarks/issues/18)) ([616d3f2](https://github.com/albertomh/django-e2e-benchmarks/commit/616d3f2442d49163e5dc8237857ea0667abefb1a))

## [0.1.2](https://github.com/albertomh/django-e2e-benchmarks/compare/v0.1.1...v0.1.2) (2025-09-09)


### Bug Fixes

* **ci:** In django-checks job, use GHA secret if in deploy mode ([#15](https://github.com/albertomh/django-e2e-benchmarks/issues/15)) ([033d528](https://github.com/albertomh/django-e2e-benchmarks/commit/033d52804c8af9e8b5f29dab3c7a09a7e62054c3))
* **ci:** Pass secret.DJANGO_SECRET_KEY as input to django-checks job ([#17](https://github.com/albertomh/django-e2e-benchmarks/issues/17)) ([c4e962c](https://github.com/albertomh/django-e2e-benchmarks/commit/c4e962cb0c74b9271dc4bb2aa9ed9c62dd0b7ce1))

## [0.1.1](https://github.com/albertomh/django-e2e-benchmarks/compare/v0.1.0...v0.1.1) (2025-09-09)


### Bug Fixes

* **ci:** Escape SECRET_KEY when generating in django-checks ([#13](https://github.com/albertomh/django-e2e-benchmarks/issues/13)) ([be09220](https://github.com/albertomh/django-e2e-benchmarks/commit/be092205b457bca59721f45948e2ae52a3095501))
* **ci:** Generate random key for django-checks action ([#12](https://github.com/albertomh/django-e2e-benchmarks/issues/12)) ([e3905d4](https://github.com/albertomh/django-e2e-benchmarks/commit/e3905d4dac24ea4d58b73fab44d19618949f6e7e))
* **ci:** Use Django secret key in webapp used by e2e in CI ([#10](https://github.com/albertomh/django-e2e-benchmarks/issues/10)) ([7756d81](https://github.com/albertomh/django-e2e-benchmarks/commit/7756d81cd23b53946cba022461a91c2489ee1910))

## 0.1.0 (2025-09-05)


### Features

* Add script to benchmark e2e tests ([#7](https://github.com/albertomh/django-e2e-benchmarks/issues/7)) ([5ccc126](https://github.com/albertomh/django-e2e-benchmarks/commit/5ccc126cf088917a8040eccc099df5a981146f66))
* **ci:** Run playwright e2e tests in CI ([#2](https://github.com/albertomh/django-e2e-benchmarks/issues/2)) ([6fdfbb7](https://github.com/albertomh/django-e2e-benchmarks/commit/6fdfbb7c404f3330a926d68dd15af546e51748c8))
* **ci:** Run pydoll e2e tests in CI ([#5](https://github.com/albertomh/django-e2e-benchmarks/issues/5)) ([e542fc4](https://github.com/albertomh/django-e2e-benchmarks/commit/e542fc48b09ad5d36deefad00bd7832224ade543))


### Bug Fixes

* **ci:** Cache Playwright browser installations ([#6](https://github.com/albertomh/django-e2e-benchmarks/issues/6)) ([b5ce9c3](https://github.com/albertomh/django-e2e-benchmarks/commit/b5ce9c3599c3c1ef7a1f8f641be84cb6c193e45b))


### Documentation

* Add section on benchmarking script to README ([#8](https://github.com/albertomh/django-e2e-benchmarks/issues/8)) ([4e186bc](https://github.com/albertomh/django-e2e-benchmarks/commit/4e186bc02713cdeb2bbba6b46d6cd290bd3aee3b))

## Changelog

Notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This file is automatically updated by Release Please.
