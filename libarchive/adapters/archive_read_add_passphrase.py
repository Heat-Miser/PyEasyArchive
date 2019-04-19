import libarchive.calls.archive_read_add_passphrase

def archive_read_add_passphrase(archive, passphrase):
    return libarchive.calls.archive_read_add_passphrase.\
            c_archive_add_passphrase(archive, passphrase)
