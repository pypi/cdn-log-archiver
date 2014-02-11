# PyPI CDN Log Archiver

1. Get yesterdays raw logs from DreamObjects, written by the cdn
2. Archive and compress them
3. Upload archive back to DreamObjects in a same structure
4. Remove raw logs

# Usage

You'll need to export some env variables to get started:

    $ export DHO_ACCESS_KEY=<your_access_key>
    $ export DHO_SECRET_KEY=<your_access_key>
    $ export PYPI_LOG_BUCKET=<bucket_name>

Now run it:

    $ python pypi-cdn-log-archiver.py
    112373 bytes written to testpypi-cdn-logs/archive/2014/2
