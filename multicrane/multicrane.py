#!/usr/bin/env python

import os,logging
from argparse import ArgumentParser
from . import version as __version__
from .util import check_running
from .crane import CraneConfig

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

def main():
    commands = [ 'lift', 'pull', 'run', 'rm', 'kill', 'status' ]
    parser = ArgumentParser(description='multicrane %s' % __version__)
    parser.add_argument('-c', dest='config_dir', help='Path to a directory \
                        containing your cranefiles', default=os.getcwd())
    parser.add_argument('command', help='Crane command to run \
                        (%s)' % ','.join(commands))

    args = parser.parse_args()

    cranes = []
    for f in os.listdir(args.config_dir):
        if 'yaml' in f or 'yml' in f: 
            cranes.append(CraneConfig(args.config_dir + "/" + f))
    log.info('successfully preloaded %d crane file(s)' % len(cranes))

    if args.command not in commands:
        log.error('Unknown command %s' % args.command)
        exit(1)
    if args.command == 'lift':
        for c in cranes:
            c.lift
    if args.command == 'pull':
        for c in cranes:
            c.pull
    if args.command == 'run':
        for c in cranes:
            c.run
    if args.command == 'rm':
        for c in cranes:
            c.rm
    if args.command == 'kill':
        for c in cranes:
            c.kill
    if args.command == 'status':
        for c in cranes:
            c.status

    print(check_running(cranes))

if __name__ == '__main__':
    main()
