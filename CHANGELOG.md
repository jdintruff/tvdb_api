# Changelog

## unreleased

- Rename exceptions to conventional PEP8 naming syntax, e.g `tvdb_error` becomes `TvdbError`, `tvdb_episodenotfound` becomes `TvdbEpisodeNotFound` etc. All exceptions have changed. Backwards-compatible bindings to old names exist until next version.
- Deprecate `Tvdb(forceConnect=...)` argument - had no effect in recent versions, and argument removed in next version.
- New `TvdbDataNotFound` exception allows catching of all missing-data exceptions in on (`TvdbShowNotFound`, `TvdbSeasonNotFound`, `TvdbEpisodeNotFound`, `TvdbResourceNotFound` are now all subclasses of this)

## `3.0.2` - 2020-05-16

- Bug fix for `ConsoleUI` error `NameError: global name 'lid_map' is not defined`

## `3.0.1` - 2020-05-11

- Reupload to PyPI to hopefully fix markdown rendering on PyPI page (may be related to [this bug](https://github.com/pypa/warehouse/issues/3664))

## `3.0` - 2020-05-11

- Important: Your own API key is now required to use this module. The default shared API key has been removed.
  Keys are easy to register via https://thetvdb.com/api-information
- Include cache location info in debug logging
- Drop support for Python 2.6 (EOL 2016), 3.3 (EOL 2013), 3.4 (EOL 2019)
- Removed deprecated `Tvdb(debug=...)` argument - use logging module instead.
  E.g `logging.basicConfig(level=logging.DEBUG)`
- Removed long deprecated `tvdb_ui` and `tvdb_exceptions` modules.
  Everything in these are accessible via the `tvdb_api` module
- Correctly errors when failing to find show by ID -
  [issue #54](https://github.com/dbr/tvdb_api/issues/54)
- Web-cache filename contains major version of Python to support
  side-by-side usage of `tvdb_api` in Python 2 and 3
- Fix bug causing occasional `KeyError` when looking up lots of shows.
  [PR #65](https://github.com/dbr/tvdb_api/pull/65)


## `2.0` - 2017-09-16

- Switch to TheTVDB new JSON based API -
  [issue #57](https://github.com/dbr/tvdb_api/issues/57)
