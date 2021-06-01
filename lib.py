import requests
import json
def post_var(pid: int,header,file):
    file_name = open(f"{file}",'r',encoding='utf-8').read()
    fields = json.loads(file_name)
    a = requests.post(url=f'https://gitlab.vieon.vn/api/v4/projects/{pid}/variables',headers=header,data=fields)
    print(a.status_code,a.text)

# if __name__ == "__main__":
#     header = {
#         'PRIVATE-TOKEN': 'zNBtw3sdCAZLvsXVGXbw'
#     }

#     a = read_var(353,header,'a.json')

#     exit(0)