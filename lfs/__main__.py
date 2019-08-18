import os

import configargparse as argparse

from lfs import get_from, client_type

parser = argparse.ArgumentParser()
parser.add_argument("uri", type=str, help="lfs uri string")
args = parser.parse_args()

print('using client: %s' % client_type())
f = get_from(args.uri)
print(f)
print(os.stat(f))
