GakuNin RDM Tools
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Developer Guide

If you are new to using `nbdev` here are some useful pointers to get you
started.

### Install grdm_tools in Development mode

``` sh
# make sure grdm_tools package is installed in development mode
$ pip install -e .

# make changes under nbs/ directory
# ...

# compile to have changes apply to grdm_tools
$ nbdev_prepare
```

## Usage

### Installation

Install latest from the GitHub
[repository](https://github.com/nakamura196/grdm-tools):

``` sh
$ pip install git+https://github.com/nakamura196/grdm-tools.git
```

### Documentation

Documentation can be found hosted on this GitHub
[repository](https://github.com/nakamura196/grdm-tools)’s
[pages](https://nakamura196.github.io/grdm-tools/).

## How to use

Initialize the `GakuNinRDM` class.

``` python
from grdm_tools.api import GrdmClient
import os

client = GrdmClient(
   token=os.environ.get('GRDM_TOKEN')
)
```

Retrieve user information.

``` python
import json

profile = client.get_users_me()

if profile:
    data = profile["data"]
    attributes = data["attributes"]
    user = {
        'id': data['id'],
        'name': attributes['full_name'],
    }
    print(json.dumps(user, indent=2))
```

    {
      "id": "hj3a6",
      "name": "Satoru Nakamura"
    }
