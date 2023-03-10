from src.jobs import read


def jobs_path(path):
    return read(path)


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    unique_job_types = []

    for job in jobs_path(path):
        if job["job_type"] not in unique_job_types:
            unique_job_types.append(job["job_type"])

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filter_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)

    return filter_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    unique_industries = []

    for job in jobs_path(path):
        if job["industry"] not in unique_industries and job["industry"] != "":
            unique_industries.append(job["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filter_jobs = [job for job in jobs if job["industry"] == industry]

    return filter_jobs


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    max_salary = 0
    salaries = set()

    for job in jobs_path(path):
        if job["max_salary"].isdigit():
            salaries.add(int(job["max_salary"]))

    max_salary = max(salaries)

    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    min_salary = 0
    salaries = set()

    for job in jobs_path(path):
        if job["min_salary"].isdigit():
            salaries.add(int(job["min_salary"]))

    min_salary = min(salaries)

    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if type(salary) is not int:
        raise ValueError("O sal??rio deve ser um n??mero inteiro")
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("O job n??o possui sal??rio m??nimo ou m??ximo")
    if type(job["min_salary"] or job["max_salary"]) != int:
        raise ValueError("O sal??rio m??nimo ou m??ximo de job n??o ?? um inteiro")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("O sal??rio m??nimo ?? maior que o m??ximo")

    return job["min_salary"] <= salary < job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filter_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_jobs.append(job)
        except ValueError:
            pass

    return filter_jobs
