export PATH := "./.venv/bin:" + env_var('PATH')

example ARG:
    go run {{ARG}}

run:
    go run main.go

bootstrap:
    pdm install

check:
    pyright

test:
    echo No unit tests yet

test-full: bootstrap check test
    #!/usr/bin/env bash -euxo pipefail
    for file in $(ls examples); do
        python3 "examples/$file"
    done

publish:
   FLIT_USERNAME="__token__" \
   FLIT_PASSWORD=$PYPI_API_TOKEN \
   flit publish

lint:
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=__pypackages__,.venv
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --ignore=F401,E501,F841,W503 --exclude=__pypackages__,.venv

doc:
    mkdir -p docs/
    fd -e rst . docs/ -x rm
    pandoc README.md -o docs/index.rst
    sphinx-apidoc -o docs plaid2/
    sphinx-build docs _build

open:
    open http://localhost:8000
    python3 -m http.server --directory _build