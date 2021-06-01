import requests
import json
def create_var(pid: int,header,file):
    file_name = open(f"{file}",'r',encoding='utf-8').read()
    fields = json.loads(file_name)
    a = requests.post(url=f'https://gitlab.vieon.vn/api/v4/projects/{pid}/variables',headers=header,data=fields)
    print('HTTP Code: ',a.status_code, '\nResult: ', a.text)

def update_var(pid: int,header,file):
    file_name = open(f"{file}",'r',encoding='utf-8').read()
    fields = json.loads(file_name)
    update_var = fields["key"]
    a = requests.put(url=f'https://gitlab.vieon.vn/api/v4/projects/{pid}/variables/{update_var}',headers=header,data=fields)
    print('HTTP Code: ',a.status_code, '\nResult: ', a.text)