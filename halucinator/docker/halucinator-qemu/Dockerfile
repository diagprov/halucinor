
FROM ubuntu:22.04 as qemu-builder

RUN apt-get update -y
RUN apt-get install -y \
        binutils binutils-dev gcc g++ make build-essential \
        pkg-config git ninja-build meson \
        zlib1g-dev libglib2.0-dev libboost-all-dev autoconf libtool \
        libssl-dev libpixman-1-dev \
        python3 libpython3-dev python3-pip python3-capstone virtualenv

RUN mkdir /build
WORKDIR /build

# shallow clone
RUN git clone --depth 1 https://github.com/HexHive/avatar-qemu.git -b dev/qemu-6.2 --recursive --shallow-submodules

RUN cd avatar-qemu && ./configure --disable-sdl \
                --disable-gtk \
                --disable-spice \
                --disable-vnc \
                --disable-tools \
                --enable-pie \
                --target-list=arm-softmmu,avr-softmmu --prefix=/opt/qemu
RUN cd avatar-qemu && make -j$(nproc) && make install

FROM ubuntu:22.04 as halucinator-qemu

ARG USER_ID
ARG GROUP_ID

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y \
        gdb-multiarch

RUN mkdir -p /opt/qemu/
COPY --from=qemu-builder /opt/qemu/* /opt/qemu/
