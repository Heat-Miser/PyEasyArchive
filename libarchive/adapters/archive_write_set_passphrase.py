import libarchive.calls.archive_write_set_passphrase

def archive_write_set_passphrase(archive, passphrase):
    return libarchive.calls.archive_write_set_passphrase.\
            c_archive_set_passphrase(archive, passphrase)
