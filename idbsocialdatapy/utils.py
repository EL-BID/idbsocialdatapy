import os

import pandas as pd

base_url = "https://scl.datamig.org/"

# -----CORE FUNCTION--------


def iadburls() -> dict:
    """
    Returns dictionary with different url strings as values
    """

    matedata_url = os.path.join(base_url, "metadata/")
    geojson_url = os.path.join(base_url, "geojson/?")
    utils_url = "&format=csv"

    url_dict = dict(
        base_urlb=base_url,  # TODO: fix base_urlb key
        utils_url=utils_url,
        matedata_url=matedata_url,
        geojson_url=geojson_url,
    )
    return url_dict


# -----GET COUNTRIES FUNCTION----------


def get_countries():
    """
    get_countries() creates a pandas dataframe.
    """
    url_links = iadburls()
    get_countries_url = os.path.join(url_links["matedata_url"], "countries")
    df = pd.read_json(get_countries_url)
    return df


# -----GET THEMES FUNCTION-----


def get_themes():
    url_links = iadburls()
    get_themes_url = os.path.join(url_links["matedata_url"], "themes")
    df = pd.read_json(get_themes_url)
    return df
