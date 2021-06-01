# GIT OPERATOR PYTHON

## USAGE

`````````
usage: main.py [-h] [--id ID] [--file FILE] {project-create-var,group-create-var}

Git operator to add environment variables to Gitlab projects/groups

positional arguments:
  {project-create-var,group-create-var}
                        Create or update project variables

optional arguments:
  -h, --help            show this help message and exit
  --id ID               Gitlab groups/projects ID
  --file FILE           Variable json file
`````````

### CREATE/UPDATE PROJECT VARIABLES

`````````
python3 main.py project-create-var --pid 353 --file a.json
`````````
`````````
python3 main.py group-create-var --pid 353 --file a.json
`````````
