import requests, json

def create_project_var(pid: int, header: dict, file: str):

    ### List các key trong project
    check = requests.get(url = f'https://gitlab.vieon.vn/api/v4/projects/{pid}/variables', headers = header).text
    check_list = [ key["key"] for key in json.loads(check) ]

    with open(file, 'r', encoding='utf-8') as f:
        file_data = f.read()
        for key in json.loads(file_data):
            if key["key"] in check_list: ### kiểm tra xem key có tồn tại trong project không
                update_request = requests.put(url = f'https://gitlab.vieon.vn/api/v4/projects/{pid}/variables/{key["key"]}', headers = header, data = key)
                print('Key: ', key["key"] , ' updated')

            else:
                create_request = requests.post(url = f'https://gitlab.vieon.vn/api/v4/projects/{pid}/variables', headers = header, data = key)
                print('Key: ', key,' created')

