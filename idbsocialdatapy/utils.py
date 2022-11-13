import os

import pandas as pd

# -----CORE FUNCTION--------


def iadburls() -> dict:
    """
    Returns dictionary with different url strings as values
    """
    base_url = "https://scl.datamig.org/"
    metadata_url = os.path.join(base_url, "metadata/")
    geojson_url = os.path.join(base_url, "geojson/?")
    utils_url = "&format=csv"

    url_dict = dict(
        base_url=base_url,
        utils_url=utils_url,
        metadata_url=metadata_url,
        geojson_url=geojson_url,
    )
    return url_dict


# -----GET COUNTRIES FUNCTION----------


def get_countries():
    """
    get_countries() creates a pandas dataframe.
    """
    url_links = iadburls()
    get_countries_url = os.path.join(url_links["metadata_url"], "countries")
    df = pd.read_json(get_countries_url)
    return df


# -----GET THEMES FUNCTION-----


def get_themes():
    url_links = iadburls()
    get_themes_url = os.path.join(url_links["metadata_url"], "themes")
    df = pd.read_json(get_themes_url)
    return df
