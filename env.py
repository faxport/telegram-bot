#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import dotenv


# Load dotenv
python_env = os.getenv('PYTHON_ENV') or 'development'
dotenv_path = os.path.join(
    os.path.dirname(__file__),
    '.env.' + python_env
)
dotenv.load_dotenv(dotenv_path)


def get(key, default=None):
    value = os.getenv(key)
    if value is None:
        return default
    return value


def must_get(key):
    value = os.getenv(key)
    if value is None:
        raise Exception('Dotenv {} is not specified.'.format(key))
    return value
