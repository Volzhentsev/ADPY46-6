import pytest
from main import *
import unittest.mock

class TestFunctions:
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    @pytest.mark.parametrize("a, result", [
        ('10006', 'Документ принадлежит: Аристарх Павлов'),
        ('3333', 'Нет такого номера документа'),
        ('11-2', 'Документ принадлежит: Геннадий Покемонов')
    ])
    def test_people_name_1(self, a, result):
        assert people_name(a) == result

    def test_people_name_2(self):
        assert people_name('123') != 'Документ принадлежит: Аристарх Павлов'

    def test_info_list(self):
        assert info_list(documents) == 'passport "2207 876234" "Василий Гупкин"'

    def test_shelf_id_1(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            assert shelf_id(directories) == '2'

    def test_shelf_id_2(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            assert shelf_id(directories) != '1'

    def test_add_info_1(self):
        with unittest.mock.patch('builtins.input', return_value='4'):
            assert add_info(documents, directories) == 'Нет такой полки'

    def test_add_info_2(self):
        with unittest.mock.patch('builtins.input', return_value='3'):
            assert add_info(documents, directories) == 'Документ добавлен'

