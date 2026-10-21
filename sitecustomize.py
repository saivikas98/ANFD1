"""Automatic interpreter startup compatibility for legacy OMCA ANFD app builds."""
import builtins
# Python name resolution falls back to builtins after local and module globals.
# This prevents legacy calls using an unscoped `polish` color variable from failing.
builtins.polish = "rgb(213,219,222)"
builtins.SS_POLISHED = "rgb(213,219,222)"
