from src.sorting import sort_by
from tests.sorting.data import (
    jobs,
    jobs_sorted_by_date_posted,
    jobs_sorted_by_max_salary,
    jobs_sorted_by_min_salary,
)


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == jobs_sorted_by_min_salary
    sort_by(jobs, "max_salary")
    assert jobs == jobs_sorted_by_max_salary
    sort_by(jobs, "date_posted")
    assert jobs == jobs_sorted_by_date_posted
