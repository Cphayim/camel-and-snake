import unittest
from camel_and_snake.converter import Converter


class TestConverter(unittest.TestCase):

    def test_camelify(self):
        """
            传入非字典、列表、元组的对象
        """
        int_val = 3
        float_val = 10.123
        bool_val = True
        str_val = 'hello'
        set_val = {1, 2, 3, 4, 5}
        none_val = None

        # 这几个测试用例都应该返回原值
        self.assertEqual(Converter.camelify(int_val), int_val)
        self.assertEqual(Converter.camelify(float_val), float_val)
        self.assertEqual(Converter.camelify(bool_val), bool_val)
        self.assertEqual(Converter.camelify(str_val), str_val)
        self.assertEqual(Converter.camelify(set_val), set_val)
        self.assertEqual(Converter.camelify(none_val), none_val)

        """
            传入一个字典
        """
        dict_obj = {
            'my_name': 'Cphayim',
            'my_like': ('Python', 'JavaScript', 'Java', 'PHP')
        }
        new_dict_obj = Converter.camelify(dict_obj)
        # my_name 被转为 myName
        self.assertEqual(
            new_dict_obj['myName'], dict_obj['my_name']
        )
        # 元组被转为列表
        self.assertEqual(
            type(new_dict_obj['myLike']), list
        )

        """
            传入一个列表
        """
        list_obj = [
            1,
            {'coder_name': 'Cphayim'},
            None
        ]
        new_list_obj = Converter.camelify(list_obj)
        # coder_name 被转为 coderName
        self.assertEqual(
            new_list_obj[1]['coderName'], list_obj[1]['coder_name']
        )

    def test_snakeify(self):
        """
            传入非字典、列表、元组的对象
        """
        int_val = 3
        float_val = 10.123
        bool_val = True
        str_val = 'hello'
        set_val = {1, 2, 3, 4, 5}
        none_val = None

        # 这几个测试用例都应该返回原值
        self.assertEqual(Converter.snakeify(int_val), int_val)
        self.assertEqual(Converter.snakeify(float_val), float_val)
        self.assertEqual(Converter.snakeify(bool_val), bool_val)
        self.assertEqual(Converter.snakeify(str_val), str_val)
        self.assertEqual(Converter.snakeify(set_val), set_val)
        self.assertEqual(Converter.snakeify(none_val), none_val)

        """
            传入一个字典
        """
        dict_obj = {
            'myName': 'Cphayim',
            'myLike': ('Python', 'JavaScript', 'Java', 'PHP')
        }
        new_dict_obj = Converter.snakeify(dict_obj)
        # myName 被转为 my_name
        self.assertEqual(
            new_dict_obj['my_name'], dict_obj['myName']
        )
        # 元组被转为列表
        self.assertEqual(
            type(new_dict_obj['my_like']), list
        )

        """
            传入一个列表
        """
        list_obj = [
            1,
            {'coderName': 'Cphayim'},
            None
        ]
        new_list_obj = Converter.snakeify(list_obj)
        # coder_name 被转为 coderName
        self.assertEqual(
            new_list_obj[1]['coder_name'], list_obj[1]['coderName']
        )


if __name__ == '__main__':
    unittest.main()
