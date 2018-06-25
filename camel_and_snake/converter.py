import re


class Converter:

    @classmethod
    def camelify(cls, obj):
        return cls.__convert(obj, target='camel')

    @classmethod
    def snakeify(cls, obj):
        return cls.__convert(obj, target='snake')

    @classmethod
    def __convert(cls, obj, target='camel'):
        # 传入对象非字典列表元祖之一，直接返回
        if type(obj) != dict and type(obj) != list and type(obj) != tuple:
            return obj

        if type(obj) == dict:
            # 当传入对象是字典, 将返回一个转换后的字典

            convert_dict = {}

            for old_key in obj:
                # 遍历字典，对每个 key 转换
                if target is 'camel':
                    new_key = re.sub(r'_(\w)', lambda match: match.group(1).upper(), old_key)
                else:
                    new_key = re.sub(r'([a-z]|\d)([A-Z])', r'\1_\2', old_key).lower()

                value = obj[old_key]
                # 对值进行递归处理
                convert_dict[new_key] = cls.__convert(value, target=target)

            return convert_dict

        else:
            # 当传入对象是列表或元组，将返回一个转换后的列表

            convert_list = []

            for item in obj:
                # 遍历每个元素，进行递归处理
                convert_list.append(cls.__convert(item, target=target))

            return convert_list
