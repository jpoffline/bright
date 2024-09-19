import json
import requests
from http import HTTPStatus
from ..models import Jobs
from abc import ABC, abstractmethod
from config import DATA_SOURCE, URL_JOBS, URL_MEMBERS
from ..vars import FILE_SOURCE, HTTP_SOURCE


class JobsDataLoader(ABC):
    @abstractmethod
    def load(self) -> Jobs:
        pass


class JobsDataFromHTTP(JobsDataLoader):
    def load(self):
        response = requests.get(URL_JOBS)
        if response.status_code != HTTPStatus.OK:
            raise Exception("cannot read jobs data")
        return Jobs.from_json(response.json())


class JobsDataFromFile(JobsDataLoader):
    file_name = "local-data/jobs.json"

    def load(self):
        with open(self.file_name) as f:
            d = json.load(f)
        return Jobs.from_json(d)


def new_data_jobs_loader(source: str):
    if source == FILE_SOURCE:
        return JobsDataFromFile()
    elif source == HTTP_SOURCE:
        return JobsDataFromHTTP()
    raise Exception("unkown source: " + source)
