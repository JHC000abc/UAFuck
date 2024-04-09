# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: __init__.py.py
@time: 2024/4/9 15:03 
@desc: 

"""

from sdk.temp.temp_supports import IsSolution, DM


class Solution(IsSolution):
    """
    Solution
    """

    def __init__(self, **kwargs):
        """
        初始化函数
        :param kwargs: 字典类型的参数字典，包含可选的关键字参数
        """
        super(Solution, self).__init__()
        self.__dict__.update({k: v for k, v in [
            i for i in locals().values() if isinstance(i, dict)][0].items()})

    def exit_handler(self):
        """
        程序退出自动执行
        :return:
        """
        print("程序退出")

    # @DM.add_project()
    def muti_thread_function(self, *args):
        """
        处理数据函数
        :param args:
        :return:
        """
        arg, file, name = args

        return None

    def process(self, **kwargs):
        """
        处理文件

        :param kwargs: 关键字参数
        :return: 无返回值
        """
        self.in_path = kwargs["in_path"]
        self.save_path = kwargs["save_path"]
        self.folder.create_folder(self.save_path)
        for file, name in self.get_file(self.in_path, status=True):
            print(file, name)  # 打印文件名和名称
            for args in self.read_line(file, _id=2):
                self.muti_thread_function(args, file, name)
                break
        DM.close_pool()


if __name__ == '__main__':
    in_path = R"D:\Desktop\1"
    save_path = R"D:\Desktop\2"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
