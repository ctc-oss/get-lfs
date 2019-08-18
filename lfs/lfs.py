import hashlib
import os

if os.system('which git-lfs > /dev/null') == os.F_OK:
    import _native as api
else:
    import _adapter as api


def is_uri(s):
    return s.startswith("lfs://")


def client_type():
    return api.client()


def get_from(uri):
    if not is_uri(uri):
        raise ValueError("uri must start with lfs://")
    splits = uri.split(":")

    ref = None
    path = splits[2]
    https = "https:%s" % splits[1]
    if https.find("@"):
        splits2 = splits[1].split("@")
        https = "https:%s" % splits2[0]
        ref = splits2[1]

    return get(path, url=https, ref=ref)


def get(path, url=None, ref=None):
    sumstr = hashlib.sha1("%s:%s" % (url, ref)).hexdigest()

    if not ref:
        ref = 'master'

    if not url or url.endswith("_"):
        if 'REPO_URL' in os.environ:
            url = os.getenv('REPO_URL')
        else:
            raise ValueError("No url was specified and REPO_URL was not set")

    wd = "/tmp/%s" % sumstr
    if not os.path.exists(wd):
        os.mkdir(wd)

    api.checkout(url, ref, [path], [], wd)
    return os.path.join(wd, path)
