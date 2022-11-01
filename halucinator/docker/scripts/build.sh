#!/bin/sh

pushd halucinator-qemu
docker build -t halucinator-qemu:6.2.0 .
popd
