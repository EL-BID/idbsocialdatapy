import os
import requests
from pandas.io.json import json_normalize
import pandas as pd

base_url = "https://scl.datamig.org/"

#-----CORE FUNCTION--------

def iadburls() -> dict:
    "Creates urls dictionary"

    matedata_url = os.path.join(base_url, "metadata/")
    geojson_url = os.path.join(base_url, "geojson/?")
    utils_url = "&format=csv"

    url_dict = dict(
        base_urlb=base_url, # base_url object converts global variable in local, making it unaccessible.
        utils_url=utils_url,
        matedata_url=matedata_url,
        geojson_url=geojson_url,
    )
    return url_dict


#-----GET COUNTRIES FUNCTION----------

def get_countries():
    """
    get_countries() creates a pandas dataframe.
    """
    url_links = iadburls()
    get_countries_url = os.path.join(url_links['matedata_url'],"countries")
    df = pd.read_json(get_countries_url)
    return dfimport os

base_url = "https://scl.datamig.org/"


def iadburls() -> dict:
    "Returns dictionary with different url strings as values"

    matedata_url = os.path.join(base_url, "metadata/")
    geojson_url = os.path.join(base_url, "geojson/?")
    utils_url = "&format=csv"

    url_dict = dict(
        base_url=base_url,
        utils_url=utils_url,
        matedata_url=matedata_url,
        geojson_url=geojson_url,
    )
    return url_dict
