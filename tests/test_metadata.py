import pytest

from idbsocialdatapy import get_countries, get_sources, get_themes, query_dictionary


@pytest.fixture
def example_get_countries():
    return get_countries()


@pytest.fixture
def example_get_themes():
    return get_themes()


@pytest.fixture
def example_get_sources():
    return get_sources()


@pytest.fixture
def example_query_dictionary():
    return query_dictionary()


columns_countries = [
    "level",
    "region_code",
    "region_name",
    "sub_region_code",
    "sub_region_name",
    "iadb_region_code",
    "iadb_region_name",
    "intermediate_region_code",
    "intermediate_region_name",
    "country_name_es",
    "country_name_en",
    "isoalpha2",
    "isoalpha3",
    "m49code",
]

columns_themes = ["theme_en", "theme_es"]

columns_sources = [
    "collection",
    "collection_en",
    "collection_es",
    "id",
    "label_es",
    "label_en",
    "description_es",
    "description_en",
    "url_collection",
    "url",
    "code",
]

columns_dictionary = [
    "collection", 
    "resource", 
    "theme_en", 
    "theme_es", 
    "indicator", 
    "label_en", 
    "label_es", 
    "description_en", 
    "description_es", 
    "valuetype", 
    "collecion_en", 
]


def test_get_countries_columns(example_get_countries):
    example_columns = example_get_countries.columns
    assert len(example_columns) == len(columns_countries)


def test_get_countries_column_identity(example_get_countries):
    assert list(example_get_countries.columns) == list(columns_countries)


def test_get_countries_shape(example_get_countries):
    example_themes = example_get_countries.shape
    assert example_themes == (26, 14)


def test_get_themes_columns(example_get_themes):
    example_columns = list(example_get_themes.columns)
    assert len(example_columns) == len(columns_themes)


def test_get_themes_column_identity(example_get_themes):
    assert list(example_get_themes.columns) == list(columns_themes)


def test_get_themes_shape(example_get_themes):
    example_themes = example_get_themes.shape
    assert example_themes == (9, 2)


def test_get_sources_columns(example_get_sources):
    example_sources = example_get_sources.columns
    assert len(example_sources) == len(columns_sources)


def test_get_sources_column_identity(example_get_sources):
    assert list(example_get_sources.columns) == list(columns_sources)


def test_get_sources_shape(example_get_sources):
    example_sources = example_get_sources.shape
    assert example_sources == (49, 11)


def test_query_dictionary_columns(example_query_dictionary):
    example_dictionary = example_query_dictionary.columns
    assert len(example_dictionary) == len(columns_dictionary)


def test_query_dictionary_column_identity(example_query_dictionary):
    assert list(example_query_dictionary.columns) == list(columns_dictionary)


def test_query_dictionary_shape(example_query_dictionary):
    example_dictionary = example_query_dictionary.shape[1]
    assert example_dictionary == (11)
