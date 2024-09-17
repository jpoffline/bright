from .models import Jobs, Members
from .loaders.members import new_data_members_loader
from .loaders.jobs import new_data_jobs_loader


def load_jobs_data() -> Jobs:
    loader = new_data_jobs_loader()
    return loader.load()


from .loaders.members import new_data_members_loader


def load_members_data() -> Members:
    loader = new_data_members_loader()
    return loader.load()
