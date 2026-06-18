FROM debian:11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

RUN apt-get update && apt-get install -y \
    texlive-fonts-recommended \
    texlive-latex-extra \
    texlive-fonts-extra \
    dvipng \
    texlive-latex-recommended \
    texlive-base \
    texlive-pictures \
    texlive-lang-cyrillic \
    texlive-science \
    cm-super \
    texlive-xetex \
    fonts-liberation \
    fonts-firacode \
    texlive-plain-generic

WORKDIR /cv

# Я делаю с WSL Windows и возникают обратные слэши, поэтому приходится их разворачивать
COPY build.sh /cv/
RUN sed -i 's/\r$//' /cv/build.sh && chmod +x /cv/build.sh

COPY main.tex /cv/
ENTRYPOINT ["/cv/build.sh"]