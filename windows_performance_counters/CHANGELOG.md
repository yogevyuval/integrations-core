# CHANGELOG - Windows performance counters

## 1.5.0 / 2022-12-09

* [Added] Implement multi-instance counters without Windows PdhEnumObjects API. See [#13243](https://github.com/DataDog/integrations-core/pull/13243).

## 1.4.0 / 2022-09-16 / Agent 7.40.0

* [Added] Refactor tooling for getting the current env name. See [#12939](https://github.com/DataDog/integrations-core/pull/12939).

## 1.3.0 / 2022-08-05 / Agent 7.39.0

* [Added] Add functionality to load the legacy version of the integration. See [#12396](https://github.com/DataDog/integrations-core/pull/12396).

## 1.2.0 / 2022-04-05 / Agent 7.36.0

* [Added] Add metric_patterns options to filter all metric submission by a list of regexes. See [#11695](https://github.com/DataDog/integrations-core/pull/11695).

## 1.1.0 / 2022-02-19 / Agent 7.35.0

* [Added] Add `pyproject.toml` file. See [#11459](https://github.com/DataDog/integrations-core/pull/11459).
* [Fixed] Fix namespace packaging on Python 2. See [#11532](https://github.com/DataDog/integrations-core/pull/11532).

## 1.0.1 / 2022-01-08 / Agent 7.34.0

* [Fixed] Add comment to autogenerated model files. See [#10945](https://github.com/DataDog/integrations-core/pull/10945).

## 1.0.0 / 2021-11-13

* [Added] Add new integration for monitoring Windows performance counters. See [#10619](https://github.com/DataDog/integrations-core/pull/10619).
