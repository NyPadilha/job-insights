from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set()

        for job in self.jobs_list:
            unique_job_types.add(job['job_type'])

        return unique_job_types

    def filter_by_multiple_criteria(self, job_list, filter_criteria) -> List[dict]:
        filtered_jobs = []

        for job in job_list:
            if all([job[key] == value for key, value in filter_criteria.items()]):
                filtered_jobs.append(job)

        return filtered_jobs
