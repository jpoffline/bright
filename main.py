from bright.data import load_jobs_data, load_members_data
from bright.matcher import match_jobs_to_member
from bright.utils import count_same_tokens


def run():

    jobs = load_jobs_data()
    members = load_members_data()

    for member in members:
        jobs_for_member = match_jobs_to_member(member, jobs)
        print(member.name, member.bio)
        for j in jobs_for_member:
            print("   " + j.title + " " + j.location)
            print(
                "      "
                + str(count_same_tokens(j.title + " " + j.location, member.bio))
            )


if __name__ == "__main__":
    run()
