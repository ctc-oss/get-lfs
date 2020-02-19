import hashlib
import os

if os.system('which git-lfs > /dev/null') == os.F_OK:
    from . import _native as api
else:
    from . import _adapter as api


def is_uri(s):
    return s.startswith("lfs://")


def client_type():
    return api.client()


def parse(uri):
    if not is_uri(uri):
        raise ValueError("uri must start with lfs://")
    splits = uri.split(":")

    ref = None
    path = splits[2]
    https = "https:%s" % splits[1]
    if https.find("@") > -1:
        splits2 = splits[1].split("@")
        https = "https:%s" % splits2[0]
        ref = splits2[1]

    # recover using environment
    if https.endswith("_") and 'REPO_URL' in os.environ:
        https = os.getenv('REPO_URL')
    if not ref:
        ref = os.environ.get('REPO_REF')

    return path, https, ref


def get(uri):
    path, https, ref = parse(uri)
    return get_from(path, url=https, ref=ref)


def get_from(path, url, ref):
    if not url or url.endswith('_'):
        raise ValueError('url must be defined')
    if not ref:
        raise ValueError('ref must be defined')

    multi = type(path) is not str and hasattr(path, "__iter__")
    paths = path if multi else [path]

    wd = checkout(url, ref, paths, [])

    files = map(lambda p: os.path.join(wd, str(p).lstrip('/')), paths)
    return files if multi else list(files)[0]


def checkout(url, ref, include, exclude):
    wd = "/tmp/%s" % hashlib.sha1(str("%s:%s" % (url, ref)).encode('utf-8')).hexdigest()
    if not os.path.isdir(os.path.join(wd, '.git')):
        if not os.path.exists(wd):
            os.mkdir(wd)

    api.checkout(url, ref, include, exclude, wd)

    return wd
