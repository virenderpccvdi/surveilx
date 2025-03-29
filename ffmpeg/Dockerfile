FROM jrottenberg/ffmpeg:latest

RUN apt-get update && apt-get install -y \
    libaom-dev \
    libvpx-dev \
    && rm -rf /var/lib/apt/lists/*

CMD ["bash"]
