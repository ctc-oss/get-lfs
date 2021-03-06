import argparse
import os
import sys

import lfs


def main(*argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("lfs_url", type=str, help="LFS repo URL")
    parser.add_argument("-r", "--ref", type=str, default='master', help="LFS data ref")
    parser.add_argument("-I", "--include", type=str, help="Inclusion pattern; empty for all")
    parser.add_argument("-X", "--exclude", type=str, help="Exclusion pattern; defaults to xview dict")
    parser.add_argument("-k", "--insecure", action='store_true', help="Skip SSL verification; GIT_SSL_NO_VERIFY")
    args = parser.parse_args(argv)

    if args.insecure:
        os.environ['GIT_SSL_NO_VERIFY'] = '1'

    includes = []
    if args.include:
        includes = args.include.split(',')

    excludes = []
    if args.exclude:
        excludes = args.exclude.split(',')

    if lfs.is_uri(args.lfs_url):
        path, url, ref = lfs.parse(args.lfs_url)
        if not ref:
            ref = args.ref
        f = lfs.get_from(path, url, ref)
    else:
        f = lfs.checkout(args.lfs_url, args.ref, includes, excludes)

    print(f)


if __name__ == "__main__":
    main(*sys.argv[1:])
