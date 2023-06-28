ARG BUILD_FROM=ghcr.io/maxwinterstein/homeassistant-adsb-multi-portal-feeder-amd64
FROM $BUILD_FROM

ENV TZ=UTC

# Add hassio sensors - thx to https://github.com/plo53
ARG version=1.1.0
# ARG sha256sum=40636f3dae484a82485f7c08cbc1f4a413e2ccf3c8b7c3a1e67651974645067d
ADD https://github.com/plo53/adsb-hassio-sensors/archive/refs/tags/${version}.tar.gz /tmp/
# RUN echo "${sha256sum}  /tmp/${version}.tar.gz" | sha256sum --check
RUN tar xvfz /tmp/${version}.tar.gz adsb-hassio-sensors-${version}/{etc,usr} --strip-components=1 -C /
