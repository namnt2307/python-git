import requests, json

def create_variable(gitlab_url: str , level: str , id: int, header: dict, file: str):

    ### List các key trong project/groups
    check = requests.get(url = f'{gitlab_url}/api/v4/{level}/{id}/variables', headers = header).text
    check_list = [ key['key'] for key in json.loads(check) ]

    with open(file, 'r', encoding = 'utf-8') as f:
        file_data = f.read()
        for key in json.loads(file_data):
            if key['key'] in check_list: ### kiểm tra xem key có tồn tại trong project/groups không
                update_request = requests.put(url = f'{gitlab_url}/api/v4/{level}/{id}/variables/{key["key"]}', headers = header, data = key)
                print('Key: ', key['key'] , ' updated')

            else:
                create_request = requests.post(url = f'{gitlab_url}/api/v4/{level}/{id}/variables', headers = header, data = key)
                print('Key: ', key['key'],' created')
