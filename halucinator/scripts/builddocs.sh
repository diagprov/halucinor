#!/bin/sh

poetry run pdoc3 --output-dir pydoc --html --force halucinator

source $(poetry env info --path)/bin/activate
poetry build
pushd doc
make html
popd
