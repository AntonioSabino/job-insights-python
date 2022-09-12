from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = {job["job_type"] for job in jobs_list if job["job_type"] != ""}
    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_list = read(path)
    industries = {
        job["industry"] for job in jobs_list if job["industry"] != ""
    }
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs_list = read(path)
    max_salary_list = {
        int(job["max_salary"])
        for job in jobs_list
        if job["max_salary"].isnumeric()
    }
    return max(max_salary_list)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary_list = {
        int(job["min_salary"])
        for job in jobs_list
        if job["min_salary"].isnumeric()
    }
    return min(min_salary_list)


def matches_salary_range(job, salary):
    if (
        "min_salary" in job
        and "max_salary" in job
        and type(job["min_salary"]) == int
        and type(job["max_salary"]) == int
        and type(salary) == int
        and job["min_salary"] < job["max_salary"]
    ):
        return salary in range(job["min_salary"], job["max_salary"])
    else:
        raise ValueError("invalid values")


def filter_by_salary_range(jobs, salary):
    salaries_in_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salaries_in_range.append(job)
        except ValueError:
            print(ValueError)
    return salaries_in_range
