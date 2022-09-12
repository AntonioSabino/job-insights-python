import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        jobs_list = []
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in jobs_reader:
            jobs_list.append(row)
        file.close()
    return jobs_list
