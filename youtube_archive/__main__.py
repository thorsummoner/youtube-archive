#!/usr/bin/env python3

import argparse
import os
import subprocess
import itertools

ARGP = argparse.ArgumentParser()
ARGP.add_argument('name')
ARGP.add_argument('--source', '-s')
ARGP.add_argument('remainder', nargs=argparse.REMAINDER)

DEFAULT_ARGS = [
    '-ciw',
]
ANNOTATE_ARGS = [
    '--add-metadata',
    '--write-description',
    '--write-annotation',
    '--write-thumbnail', 
]
ARIA2C_ARGS = [
    '--external-downloader=aria2c',
    '--external-downloader-args=-c -j 16 -x 16 -s 16 -k 1M',
]

def main(argp=None):
    if argp is None:
        argp = ARGP.parse_args()
        if argp.source:
            argp.source = argp.source.strip()

    if argp.source and not os.path.exists(argp.name):
        os.makedirs(argp.name)
    
    source = os.path.join(argp.name, '.source')
    if not os.path.exists(source):
        assert argp.source
        with open(source, 'w') as sourcefd:
            sourcefd.write('{}\n'.format(argp.source))

    with open(source) as sourcefd:
        link = sourcefd.read().strip()

    subprocess.check_call(
        itertools.chain(
            ['youtube-dl', link],
            DEFAULT_ARGS,
            ANNOTATE_ARGS,
            ARIA2C_ARGS,
            argp.remainder,
        ),
        cwd=argp.name,
    )
if __name__ == '__main__':
    main()

