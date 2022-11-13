import pytest

from idbsocialdatapy.metadata import get_countries, get_themes


@pytest.fixture
def example_get_countries():
    return get_countries()


@pytest.fixture
def example_get_themes():
    return get_themes()


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


def test_get_themes_column_identity(example_get_themes):  # FALLA
    assert list(example_get_themes.columns) == list(columns_themes)


def test_get_themes_shape(example_get_themes):
    example_themes = example_get_themes.shape
    assert example_themes == (11, 2)
