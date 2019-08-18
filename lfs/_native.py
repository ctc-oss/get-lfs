from git import InvalidGitRepositoryError
from git import Repo


def client():
    return 'native'


def checkout(url, ref, include, exclude, dest):
    try:
        r = Repo(dest)
    except InvalidGitRepositoryError:
        Repo.clone_from(url, dest, b=ref)
        r = Repo(dest)

    fetch_cmd = ['git', 'lfs', 'fetch']
    if include:
        fetch_cmd.extend(['-I', ','.join(include)])
    if exclude:
        fetch_cmd.extend(['-X', ','.join(include)])

    g = r.git
    g.execute(fetch_cmd)
    g.execute(['git', 'lfs', 'checkout'])
