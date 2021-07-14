import requests
import json
import argparse
import gitlab.v4.objects
import re


def create_variable(
        gitlab_url: str,
        level: str,
        id: int,
        header: dict,
        file: str):

    # List các key trong project/groups
    check = requests.get(
        url=f'{gitlab_url}/api/v4/{level}/{id}/variables',
        headers=header
    ).text
    check_list = [key['key'] for key in json.loads(check)]

    with open(file, 'r', encoding='utf-8') as f:
        file_data = f.read()
        for key in json.loads(file_data):
            if key['key'] in check_list:  # kiểm tra xem key có tồn tại trong project/groups khg
                update_request = requests.put(
                    url=f'{gitlab_url}/api/v4/{level}/{id}/variables/{key["key"]}',
                    headers=header,
                    data=key)
                print('Key: ', key['key'], ' updated')
            else:
                create_request = requests.post(
                    url=f'{gitlab_url}/api/v4/{level}/{id}/variables',
                    headers=header,
                    data=key
                )
                print('Key: ', key['key'], ' created')


def get_id(gitlab_url: str, level: str, id: int, header: dict):

    pass


def trigger(gitlab_url: str, id: int, header: dict, ref: str, extra_var: str):

    data = {
        'ref': ref,
        'variables': []
    }
    variables = extra_var.split(',')
    for x in variables:
        if re.match('\\w=\\w', x):
            data['variables'].append({
                'key': x.split('=')[0],
                'value': x.split('=')[1]
            })
    r = requests.post(
        url=f'{gitlab_url}/api/v4/projects/{id}/pipeline',
        headers=header,
        json=data)
