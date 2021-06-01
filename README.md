# GIT OPERATOR PYTHON

## USAGE

`````````
usage: main.py [-h] [--pid PID] [--file FILE] {project-create,group-create}

Git operator to add environment variables to Gitlab projects/groups

positional arguments:
  {project-create,group-create}
                        Create or update project variables

optional arguments:
  -h, --help            show this help message and exit
  --pid PID             Gitlab project ID
  --file FILE           Variable json file
`````````

### CREATE/UPDATE PROJECT VARIABLES

`````````
python3 main.py project-create --pid 353 --file a.json
`````````
