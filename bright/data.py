from .models import Jobs, Members
from .loaders.members import new_data_members_loader
from .loaders.jobs import new_data_jobs_loader
from .loaders.members import new_data_members_loader


def load_jobs_data(source: str) -> Jobs:
    loader = new_data_jobs_loader(source)
    return loader.load()


def load_members_data(source: str) -> Members:
    loader = new_data_members_loader(source)
    return loader.load()
