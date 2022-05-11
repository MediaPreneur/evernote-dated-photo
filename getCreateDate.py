import EXIF
import sys
import os.path

def formatDate(date):
    "YYYY:MM:DD HH:MM:SS"
    d = date.split(' ')[0]
    y,m,d = d.split(':')
    return f'{m}/{d}/{y[2:]}'

if sys.argv[1] and os.path.exists(sys.argv[1]):
    with open(sys.argv[1].strip(),'rb') as fd:
        tags = EXIF.process_file(fd)
    if tags.has_key('EXIF DateTimeOriginal'):
        d = str(tags['EXIF DateTimeOriginal'])
        sys.stdout.write(formatDate(d))
