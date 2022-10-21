from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        list_of_dicts = list(content)

    return list_of_dicts
