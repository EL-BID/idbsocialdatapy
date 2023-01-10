import os


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
