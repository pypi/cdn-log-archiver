#!/usr/bin/env python

import os
import sys
import shutil
from tempfile import mkdtemp
import tarfile
import boto
import boto.s3.connection
from contextlib import contextmanager
from datetime import date


@contextmanager
def temp_directory():
    temp_dir = mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


def tar_logs(tar_file, tar_dir):
    archive = tarfile.open(tar_file, 'w:gz')
    archive.add(tar_dir, arcname='')
    archive.close()


def write_logs_to_temp(todays_logs, dest):
    [l.get_contents_to_filename('{0}/{1}'.format(dest, l.name[9:])) for l in
        todays_logs]


def archive_logs(bucket, todays_logs, save_to, todays_date):
    bytes_written = 0
    with temp_directory() as temp_dir:
        tar_file = os.path.join(temp_dir, "../{0}.tar.gz".format(todays_date))
        write_logs_to_temp(todays_logs, temp_dir)
        tar_logs(tar_file, temp_dir)

        new_archive = bucket.new_key(os.path.join(save_to,
                                     os.path.basename(tar_file)))

        bytes_written = new_archive.set_contents_from_filename(tar_file)
        os.remove(tar_file)

    return bytes_written


def remove_raw_logs(bucket, todays_logs):
    [bucket.delete_key(l) for l in todays_logs]


def collect_todays_logs(bucket, look_for):
    return [k for k in bucket.list() if k.name.startswith(look_for)]


def main():
    access_key = os.environ['DHO_ACCESS_KEY']
    secret_key = os.environ['DHO_SECRET_KEY']
    bucket_name = os.environ['PYPI_LOG_BUCKET']
    todays_date = str(date.today())
    look_for = 'incoming/{0}'.format(todays_date)
    save_to = 'archive/{0}/{1}'.format(date.today().year,
                                       date.today().month)

    conn = boto.connect_s3(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        host='objects.dreamhost.com',
        calling_format=boto.s3.connection.OrdinaryCallingFormat()
    )

    bucket = conn.get_bucket(bucket_name)

    todays_logs = collect_todays_logs(bucket, look_for)
    bytes_written = archive_logs(bucket, todays_logs, save_to, todays_date)
    remove_raw_logs(bucket, todays_logs)

    if bytes_written and bytes_written > 0:
        print('{0} bytes written to {1}/{2}'.format(bytes_written,
                                                    bucket_name, save_to))
        return 0
    else:
        print('Nothing written to {0}/{1}'.format(bucket_name, save_to))
        return 1


if __name__ == '__main__':
    sys.exit(main())
