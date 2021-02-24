"""
读取数据
"""
import configparser
import ast
import json
import os
import yaml


def read_ini(file_path, key):
    """
    读取配置文件
    :param file_path: 配置文件路径
    :param key: 配置文件中的key
    :return: 返回key所对应的value
    """
    config = configparser.ConfigParser()
    file_path = get_project_path() + file_path
    config.read(file_path)
    #
    value = config.get('env', key)
    return value


def get_project_path():
    """
    获取工作路径
    :return: 配置文件的绝对路径对应的目录
    """
    # 当前文件路径
    file_path = os.path.realpath(__file__)
    # 当前文件所在目录
    dir_path = os.path.dirname(file_path)
    # 上一级目录
    dir_path = os.path.dirname(dir_path)
    return dir_path + '\\'


def read_yaml(file_path):
    file_path = get_project_path() + file_path
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        content = yaml.load(file_content, Loader=yaml.FullLoader)
        return content


if __name__ == '__main__':
    # v = read_ini(r'test_env\env.ini', 'db_info')
    # s = ast.literal_eval(v)
    # print(s["host"])
    #
    # # json格式转字典
    # x = read_ini(r'test_env\env.ini', 'db_info')
    # print(json.loads(x)["host"])
    #
    # print(read_yaml(r"test_data\register_fail.yaml")[0]['data'])

    content = read_yaml(r"test_data\register_fail.yaml")
    print(content)