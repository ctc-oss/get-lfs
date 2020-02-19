import os

import argparse
import lfs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lfs_url", type=str, help="LFS repo URL")
    parser.add_argument("-r", "--ref", type=str, default='master', help="LFS data ref")
    parser.add_argument("-I", "--include", type=str, help="Inclusion pattern; empty for all")
    parser.add_argument("-X", "--exclude", type=str, help="Exclusion pattern; defaults to xview dict")
    args = parser.parse_args()

    includes = []
    if args.include:
        includes = args.include.split(',')

    excludes = []
    if args.exclude:
        excludes = args.exclude.split(',')

    wd = lfs.checkout(args.lfs_url, args.ref, includes, excludes)

    print(wd)
