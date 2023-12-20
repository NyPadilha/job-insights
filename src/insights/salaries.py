from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salaries = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job.get("max_salary", "").isdigit()
        ]

        return max(max_salaries)

    def get_min_salary(self) -> int:
        min_salaries = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job.get("min_salary", "").isdigit()
        ]

        return min(min_salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        min_salary, max_salary = job.get("min_salary"), job.get("max_salary")

        try:
            salary = int(salary)
            min_salary = int(min_salary)
            max_salary = int(max_salary)
        except (ValueError, TypeError):
            raise ValueError("salary is not a number")

        if min_salary > max_salary:
            raise ValueError("minimum salary is greater than maximum salary")

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        filtered_jobs = list()

        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    filtered_jobs.append(job)
            except ValueError:
                False

        return filtered_jobs
