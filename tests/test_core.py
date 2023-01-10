import pandas as pd
import pytest

from idbsocialdatapy import query_indicator, search_indicator


def test_search_indicator_invalid_input_type():
    with pytest.raises(TypeError):
        search_indicator(1)


def test_search_indicator_invalid_input_len():
    with pytest.raises(ValueError):
        search_indicator("")


def test_search_indicator_empty_output():
    with pytest.raises(pd.errors.EmptyDataError):
        search_indicator("false_input")


def test_search_indicator_output_type():
    assert isinstance(search_indicator("pobreza"), pd.DataFrame)


def test_query_indicator_invalid_input_type():
    with pytest.raises(TypeError):
        query_indicator(1)


def test_query_indicator_invalid_input_len():
    with pytest.raises(ValueError):
        query_indicator("")


def test_query_indicator_empty_output():
    with pytest.raises(pd.errors.EmptyDataError):
        query_indicator("false_input")


def test_query_indicator_output_type():
    assert isinstance(query_indicator("pobreza"), pd.DataFrame)
