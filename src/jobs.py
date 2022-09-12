from csv import DictReader
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        jobs_list = []
        jobs_reader = DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_reader:
            jobs_list.append(job)
        file.close()
    return jobs_list
