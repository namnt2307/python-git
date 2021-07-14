import os
import argparse
import func
GITLAB_PRIVATE_TOKEN = os.getenv(
    "GITLAB_PRIVATE_TOKEN", 'zNBtw3sdCAZLvsXVGXbw')
GITLAB_URL = os.getenv("GITLAB_URL", 'https://gitlab.vieon.vn')

header = {"PRIVATE-TOKEN": GITLAB_PRIVATE_TOKEN}

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="pygit",
        description="Git operator to add environment variables to Gitlab projects/groups",
    )
    parser.add_argument(
        "action",
        help="Upsert variables, get project id, trigger pipeline",
        choices=["upsert", "list", "trigger"],
    )
    parser.add_argument("--type", help="Project or Group level", dest="level")
    parser.add_argument(
        "--id", help="Gitlab groups/projects ID", type=int, dest="id")
    parser.add_argument("--file", help="Variable json file",
                        type=str, dest="file")
    parser.add_argument(
        "--per", help="Display more objects per page", type=int, dest="per"
    )
    parser.add_argument(
        "-e", help="Extra variables for pipeline", type=str, dest="extra_vars"
    )
    parser.add_argument(
        "--ref", help="Branch", type=str, dest="ref"
    )

    args = parser.parse_args()

    if GITLAB_PRIVATE_TOKEN is None or GITLAB_URL is None:
        print(
            """Please set GITLAB_PRIVATE_TOKEN and GITLAB_URL before using pygit
        """
        )
        exit(1)

    if args.action == "upsert":
        func.upsert_variable(GITLAB_URL, args.level,
                             args.id, header, args.file)
    if args.action == "list":
        pass
    if args.action == "trigger":
        func.trigger(GITLAB_URL, args.id, header, args.ref, args.extra_vars)
    exit(0)
