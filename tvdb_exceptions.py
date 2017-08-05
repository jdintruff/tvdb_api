#!/usr/bin/env python
#encoding:utf-8
#author:dbr/Ben
#project:tvdb_api
#repository:http://github.com/dbr/tvdb_api
#license:unlicense (http://unlicense.org/)

"""Custom exceptions used or raised by tvdb_api
"""

__author__ = "dbr/Ben"
__version__ = "1.10"

import logging

__all__ = ["tvdb_error", "tvdb_userabort", "tvdb_shownotfound",
"tvdb_seasonnotfound", "tvdb_episodenotfound", "tvdb_attributenotfound"]

logging.getLogger(__name__).warning(
    "tvdb_exceptions module is deprecated - use classes directly from tvdb_api instead")

from tvdb_api import (
    tvdb_error, tvdb_userabort, tvdb_shownotfound,
    tvdb_seasonnotfound, tvdb_episodenotfound, tvdb_attributenotfound
)
