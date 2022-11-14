from typing import Union

import pandas as pd
import requests

from .utils import iadburls


def search_indicator(
    search: str,
    countries: Union[str, list] = "All",
    yearstart: Union[str, int] = "All",
    yearend: Union[str, int] = "All",
) -> pd.DataFrame:
    """Search for indicator using words and filters.

    Parameters
    ----------
    search : str
        indicator name
     countries : Union[str, list], optional
        list or comma separated alpha-3 country codes, by default 'All'
    yearstart : Union[str, int], optional
        start year, by default 'All'
    yearend : Union[str, int], optional
        end year, by default 'All'

    Returns
    -------
    pd.DataFrame
        data frame with found indicators

    Raises
    ------
    TypeError
        if search parameter is not a string
    ValueError
        if search parameter is an empty string
    pd.errors.EmptyDataError
        if used values return no results
    """
    if not isinstance(search, str):
        raise TypeError("search parameter must be a string")
    if len(search) == 0:
        raise ValueError("search parameter must be a non empty string")
    if isinstance(countries, list):
        countries = ",".join(countries)

    urls = iadburls()
    url = urls["base_url"] + "data/search?words=" + search

    if countries != "All":
        url = url + "&countries=" + countries
    if yearstart != "All":
        url = url + "&yearstart=" + str(yearstart)
    if yearend != "All":
        url = url + "&yearend=" + str(yearend)

    json_data = requests.get(url).json()["data"]
    data = pd.DataFrame(json_data)
    if data.empty:
        err_string = "no results were found for specified parameters"
        raise pd.errors.EmptyDataError(err_string)
    return data


def query_indicator(
    indicator: str,
    categories: Union[str, list] = "All",
    countries: Union[str, list] = "All",
    yearstart: Union[str, int] = "All",
    yearend: Union[str, int] = "All",
    year: Union[str, int] = "All",
    latest: bool = False,
):
    """Get available data about selected indicator.

    Parameters
    ----------
    indicator : str
        Selected indicator
    categories : Union[str, list], optional
        list or comma separated categories, by default 'All'
    countries : Union[str, list], optional
        list or comma separated alpha-3 country codes, by default 'All'
    yearstart : Union[str, int], optional
        start year, by default 'All'
    yearend : Union[str, int], optional
        end year, by default 'All'
    year : Union[str, int], optional
        year, by default 'All'
    latest : bool, optional
        Whether to retrieve the latest data point available, by default False

    Returns
    -------
    pd.DataFrame
        data frame with results for selected indicator

    Raises
    ------
    TypeError
        if indicator parameter is not a string
    ValueError
        if indicator parameter is an empty string
    pd.errors.EmptyDataError
        if used values return no results
    """

    if not isinstance(indicator, str):
        raise TypeError("indicator parameter must be a string")
    if len(indicator) == 0:
        raise ValueError("indicator parameter must be a non empty string")
    if isinstance(countries, list):
        countries = ",".join(countries)
    if isinstance(categories, list):
        categories = ",".join(categories)

    urls = iadburls()
    url = urls["base_url"] + "data?indicators=" + indicator

    if countries != "All":
        url = url + "&countries=" + countries
    if categories != "All":
        url = url + "&categories=" + categories
    if yearstart != "All":
        url = url + "&yearstart=" + str(yearstart)
    if yearend != "All":
        url = url + "&yearend=" + str(yearend)
    if year != "All":
        url = url + "&year=" + str(year)
    if latest:
        url = url + "&latest"

    json_data = requests.get(url).json()["data"]
    data = pd.DataFrame(json_data)
    if data.empty:
        err_string = "no results were found for specified parameters"
        raise pd.errors.EmptyDataError(err_string)
    if "dt" in data.columns:
        data["dt"] = pd.to_datetime(data["dt"])
    return data
