#pip install requests

import requests

def get_server_time(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            server_time = data.get('server_time')
            return server_time
        else:
            print(f"Failed to fetch server time. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# 替换为您要查询的 API URL
api_url = "https://api.example.com/get_server_time"

server_time = get_server_time(api_url)

if server_time:
    print(f"Server time: {server_time}")
