from yandex_data import YaUploader
token = ' '# токен к яндекс диску
uploader = YaUploader(token)

class TestFunctions:
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_create_ya_folder(self):
        assert uploader.create_ya_folder('Test13') == 201

    def test_delete_ya_folder(self):
        assert uploader.delete_ya_folder('Test13') == 204