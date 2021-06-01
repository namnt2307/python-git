import os
import argparse
from lib import post_var
GITLAB_PRIVATE_TOKEN = os.getenv('GITLAB_PRIVATE_TOKEN',None)
header = {}
if __name__ == "__main__":
    
    if GITLAB_PRIVATE_TOKEN == None:
        print("""Please set GITLAB_PRIVATE_TOKEN before using pygit        
        """)
        exit(1)
    else:
        header = {
            'PRIVATE-TOKEN': f'{GITLAB_PRIVATE_TOKEN}'
        }
    parser = argparse.ArgumentParser(description="Git operator to add environment variables to Gitlab projects/groups")
    parser.add_argument('action',help="Create project variables",choices=["create","update"])
    parser.add_argument('--pid',help="Gitlab project ID",type=int,dest='pid')
    parser.add_argument('--file',help="Variable json file",type=str,dest='file')

    args = parser.parse_args()

    if args.action == "create":
        # print(args.pid,header,args.file)
        post_var(args.pid,header,args.file)
    else:
        pass



    exit(0)
