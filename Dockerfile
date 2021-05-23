FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade numpy
RUN pip install --upgrade autopep8
RUN pip install --upgrade atcoder-tools

# Default setting for atcodertools
RUN echo "[codestyle]" >> /root/.atcodertools.toml
RUN echo "workspace_dir='/workspaces/atcoder/src'" >> /root/.atcodertools.toml
RUN echo "lang='python'" >> /root/.atcodertools.toml

# Fix to avoid submit error
RUN sed -i -e 's/Python3/Python/' /usr/local/lib/python3.9/site-packages/atcodertools/common/language.py
