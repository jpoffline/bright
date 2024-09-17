from bright.data import load_jobs_data, load_members_data
from bright.matcher import match_jobs_to_member


def run():

    jobs = load_jobs_data()
    members = load_members_data()

    print(match_jobs_to_member(members[0], jobs))
    print(members[1].bio, match_jobs_to_member(members[1], jobs))
    print(match_jobs_to_member(members[2], jobs))
    print(match_jobs_to_member(members[3], jobs))


if __name__ == "__main__":
    run()
