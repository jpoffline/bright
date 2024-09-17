from dataclasses import dataclass, field
from typing import List


@dataclass
class Member:
    name: str
    bio: str

    @property
    def lower_bio(self):
        return self.bio.lower()

    @classmethod
    def from_json(cls, j):
        return cls(name=j["name"], bio=j["bio"])


@dataclass
class Members:
    members: List[Member] = field(default_factory=list)

    def __iter__(self):
        for m in self.members:
            yield m

    @classmethod
    def from_json(cls, js):
        return [Member.from_json(j) for j in js]


@dataclass
class Job:
    title: str
    location: str

    @property
    def lower_title(self):
        return self.title.lower()

    @property
    def lower_location(self):
        return self.location.lower()

    @classmethod
    def from_json(cls, j):
        return cls(location=j["location"], title=j["title"])


@dataclass
class Jobs:
    jobs: List[Job] = field(default_factory=list)

    def __iter__(self):
        for job in self.jobs:
            yield job

    @classmethod
    def from_json(cls, js):
        return [Job.from_json(j) for j in js]
