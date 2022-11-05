import pytest
import os
from pandas.io.json import json_normalize
import pandas as pd
from idbsocialdatapy.utils import iadburls



@pytest.fixture
def example_iadburls():
    return iadburls()


def test_iadburls_len(example_iadburls):
    assert len(example_iadburls) == 4


def test_iadburls_type(example_iadburls):
    assert isinstance(example_iadburls, dict)


def test_iadburls_keys(example_iadburls):
    keys = example_iadburls.keys()
    for key in keys:
        assert key in ("base_urlb", "utils_url", "matedata_url", "geojson_url")


def test_iadburls_values(example_iadburls):
    values = example_iadburls.values()
    for value in values:
        assert value in (
            "https://scl.datamig.org/",
            "https://scl.datamig.org/metadata/",
            "&format=csv",
            "https://scl.datamig.org/geojson/?",
        )
