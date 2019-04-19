from ctypes import *

from libarchive.library import libarchive
from libarchive.constants.archive import *

def _check_zero_success(value):
    if value != ARCHIVE_OK:
        raise ValueError("Function returned failure: (%d)" % (value))

    return value

c_archive_write_set_passphrase = libarchive.archive_write_set_passphrase
c_archive_write_set_passphrase.argtypes = [c_void_p, c_char_p]
c_archive_write_set_passphrase.restype = c_int
