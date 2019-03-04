# camel-and-snake

[![Build Status](https://travis-ci.org/Cphayim/camel-and-snake.svg?branch=master)](https://travis-ci.org/Cphayim/camel-and-snake)
[![PyPI version](https://badge.fury.io/py/camel-and-snake.svg)](https://badge.fury.io/py/camel-and-snake)
![Python version](https://img.shields.io/badge/python-3.3+-blue.svg)

## 🐫 and 🐍 ？？？🤣

本项目旨在解决 camelCase 和 snake_case 相互转换的问题

**支持 python3 以上版本**


## 应用场景

* 生成对 JavaScript 更友好的 `camelCase` 命名规范的 JSON 响应数据
    * 在 JSON 序列化之前将 `snake_case` 的字典转为 `camelCase`
    * 在 JSON 反序列化之后将 `camelCase` 的字典转回 `snake_case`


## 如何使用？

### 安装

你可以通过 `pip` 来安装 `camel_and_snake`
> 推荐使用 `pipenv` 在虚拟环境下安装

```shell
$ pip3 install camel_and_snake
```


### 使用

```python
from camel_and_snake import Converter
```

**snake_case -> camelCase**

```python
dict_obj = {
    'org_id': 123,
    'org_name': 'ShadowCoder',
    'member_list': [
        {'member_id': 1, 'member_name': 'Cphayim'},
        {'member_id': 2, 'member_name': 'Hoyoe'}
    ]
}

# 转换过程中将递归对深层的每一个字典进行替换 key 值，并返回一个新的对象
json.dumps(Converter.camelify(dict_obj), indent=2)

"""
{
  "orgId": 123,
  "orgName": "ShadowCoder",
  "memberList": [
    {
      "memberId": 1,
      "memberName": "Cphayim"
    },
    {
      "memberId": 2,
      "memberName": "Hoyoe"
    }
  ]
}
"""
```


**camelCase -> snake_case**

```python
json_str = '{"orgId": 123, "orgName": "ShadowCoder", "memberList": [{"memberId": 1, "memberName": "Cphayim"}, {"memberId": 2, "memberName": "Hoyoe"}]}'

dict_obj = Converter.snakeify(json.loads(json_str))
# {'org_id': 123, 'org_name': 'ShadowCoder', 'member_list': [{'member_id': 1, 'member_name': 'Cphayim'}, {'member_id': 2, 'member_name': 'Hoyoe'}]}
```

## License

[MIT](https://opensource.org/licenses/MIT)
