import os
import argparse
from lib import create_variable

GITLAB_PRIVATE_TOKEN = os.getenv('GITLAB_PRIVATE_TOKEN', None)
GITLAB_URL = os.getenv('GITLAB_URL', None)

header = {
    'PRIVATE-TOKEN': GITLAB_PRIVATE_TOKEN
    }

if __name__ == "__main__":
    
    if GITLAB_PRIVATE_TOKEN == None:
        print(
        """Please set GITLAB_PRIVATE_TOKEN before using pygit        
        """
        )
        exit(1)
    elif GITLAB_URL == None:
        print(
        """Please set GITLAB_URL before using pygit        
        """
        )
        exit(1)    

    parser = argparse.ArgumentParser(description="Git operator to add environment variables to Gitlab projects/groups")
    parser.add_argument('action', help="Create or update project variables", choices=["project-create-var","group-create-var"])
    parser.add_argument('--id', help="Gitlab groups/projects ID", type=int, dest='id')
    parser.add_argument('--file', help="Variable json file", type=str, dest='file')

    args = parser.parse_args()

    if args.action == "project-create-var":
        create_variable(GITLAB_URL, 'projects',args.id, header, args.file)
    elif args.action == "group-create-var":
        create_variable(GITLAB_URL, 'groups',args.id, header, args.file)
   
    exit(0)
        
