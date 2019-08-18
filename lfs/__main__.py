import os

import configargparse as argparse

from lfs import get, get_from, client_type, parse

parser = argparse.ArgumentParser()
parser.add_argument("uri", type=str, help="lfs uri string")
args = parser.parse_args()

print('using repo uri: %s' % args.uri)
print('using client: %s' % client_type())
f = get(args.uri)
print(f)
print(os.stat(f))

_, https, ref = parse(args.uri)
f = get_from('train/80.geojson', ref=ref, url=https)
print(f)
print(os.stat(f))
