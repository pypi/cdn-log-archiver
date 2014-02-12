# PyPI CDN Log Archiver

1. Get raw logs from DreamObjects, written by the cdn
2. Archive and compress them
3. Upload archive back to DreamObjects in a sane structure
4. Remove raw logs that were archived

# Usage

You'll need to export some env variables to get started:

    $ export DHO_ACCESS_KEY=<your_access_key>
    $ export DHO_SECRET_KEY=<your_access_key>
    $ export PYPI_LOG_BUCKET=<bucket_name>

Optionally you can set the date to archive like so:

    $ export PYPI_LOG_DATE=2014-02-11

If you don't set `PYPI_LOG_DATE`, the script will default to looking for
yesterdays date.

Now you should be able to run it:

    $ python pypi-cdn-log-archiver.py
    112373 bytes written to testpypi-cdn-logs/archive/2014/2
