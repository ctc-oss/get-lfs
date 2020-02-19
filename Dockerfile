FROM python:3.6

ARG LFS_VERSION="v2.10.0"
ENV PYTHONPATH=/opt/src

RUN mkdir -p /tmp/lfs/src \
 && curl -sL -o /tmp/lfs/lfs.tar.gz "https://github.com/git-lfs/git-lfs/releases/download/${LFS_VERSION}/git-lfs-linux-amd64-${LFS_VERSION}.tar.gz" \
 && tar xvzf /tmp/lfs/lfs.tar.gz -C /tmp/lfs/src \
 && /tmp/lfs/src/install.sh \
 && git lfs install --skip-smudge \
 && rm -rf /tmp/lfs

WORKDIR /opt/src
COPY . /opt/src

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "lfs"]
