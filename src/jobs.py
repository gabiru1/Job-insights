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
    with open(path, encoding="utf-8") as file:
        jobs = csv.DictReader(file)

        filter_jobs = []

        for job in jobs:
            filter_jobs.append(job)

        return filter_jobs


read("src/jobs.csv")
