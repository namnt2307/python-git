# GIT OPERATOR PYTHON

## USAGE
### CREATE PROJECT VARIABLES
`````````
usage: main.py [-h] [--pid PID] [--file FILE] {create,update}

Git operator to add environment variables to Gitlab projects/groups

positional arguments:
  {create,update}  Create project variables

optional arguments:
  -h, --help       show this help message and exit
  --pid PID        Gitlab project ID
  --file FILE      Variable json file
`````````
`````````
python3 main.py create --pid 353 --file a.json
`````````
### UPDATE PROJECT VARIABLES
`````````
python3 main.py update --pid 353 --file a.json
`````````