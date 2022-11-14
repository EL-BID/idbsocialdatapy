import os

import pandas as pd

from idbsocialdatapy import iadburls


def get_countries():
    """
    get_countries() creates a pandas dataframe.
    """
    url_links = iadburls()
    get_countries_url = os.path.join(url_links["metadata_url"], "countries")
    df = pd.read_json(get_countries_url)
    return df


def get_themes():
    url_links = iadburls()
    get_themes_url = os.path.join(url_links["metadata_url"], "themes")
    df = pd.read_json(get_themes_url)
    return df


def query_dictionary(indicator="All"):
    """
    Returns dictionary as a pandas dataframe
    """
    url_links = iadburls()
    get_dictionary_url = os.path.join(url_links["metadata_url"], "dictionary?")

    if indicator != "All":
        get_dictionary_url = get_dictionary_url + "&indicator=" + indicator

    df = pd.read_json(get_dictionary_url)
    return df
