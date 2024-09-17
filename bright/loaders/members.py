import json
import requests
from http import HTTPStatus
from ..models import Members
from abc import ABC, abstractmethod
from config import DATA_SOURCE, URL_MEMBERS
from ..vars import FILE_SOURCE, HTTP_SOURCE


class MembersDataLoader(ABC):
    @abstractmethod
    def load(self) -> Members:
        pass


class MembersDataFromHTTP(MembersDataLoader):
    def load(self):
        response = requests.get(URL_MEMBERS)
        if response.status_code != HTTPStatus.OK:
            raise Exception("cannot read members data")
        return Members.from_json(response.json())


class MembersDataFromFile(MembersDataLoader):
    file_name = "local-data/members.json"

    def load(self):
        with open(self.file_name) as f:
            d = json.load(f)
        return Members.from_json(d)


def new_data_members_loader():
    if DATA_SOURCE == FILE_SOURCE:
        return MembersDataFromFile()
    elif DATA_SOURCE == HTTP_SOURCE:
        return MembersDataFromHTTP()
    raise Exception("unkown source: " + DATA_SOURCE)
