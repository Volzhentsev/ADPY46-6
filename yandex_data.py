import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_ya_folder(self, folder_name: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": folder_name}
        response = requests.put(url=url, headers=headers, params=params)
        response.raise_for_status()
        return response.status_code
        # if response.status_code == 201:
        #     print(f'Папка создана, {response.status_code}')

    def delete_ya_folder(self, folder_name: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": folder_name}
        delete = requests.delete(url=url, headers=headers, params=params)
        return delete.status_code



if __name__ == '__main__':
    token = ' '# токен к яндекс диску
    uploader = YaUploader(token)
    result = uploader.create_ya_folder('test85')
    result_2 = uploader.delete_ya_folder('test85')
