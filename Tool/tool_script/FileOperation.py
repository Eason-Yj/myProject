import os
import sys
import shutil
import re
from typing import Union, Optional, List
import logging


class file_process():
    """
    对文件(夹)进行批量操作
    """

    def __init__(self, origin_path, target_path=None):  # type:(str, Optional[str])->None
        """

        Parameters
        ----------
        origin_path 源文件(夹)路径
        target_path 目标文件(夹)路径
        """
        self.origin_path = origin_path
        self.target_path = target_path
        self._checkout()

    def _checkout_is_file(self, path):
        if not os.path.exists(path):
            raise ValueError("路径不存在：{}".format(path))
        if not os.path.isfile(path):
            raise ValueError("路径需要为文件：{}".format(path))

    def _checkout_is_dir(self, path):
        file_name = os.path.basename(path)
        if "." in file_name:
            raise ValueError("路径需要未文件夹：{}".format(path))

    def _checkout(self):
        if not isinstance(self.origin_path, str):
            raise TypeError("源文件路径需要为字符串格式，当前为:{}".format(type(self.origin_path)))
        if self.target_path is not None and not isinstance(self.target_path, str):
            raise TypeError("目标文件路径需要为字符串格式，当前为:{}".format(type(self.target_path)))
        if not os.path.exists(self.origin_path):
            raise ValueError("路径不存在：{}".format(self.origin_path))

    @staticmethod
    def _delete_file(file_path):  # type:(Union[list,str])->None
        def _delete(path):
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)

        if isinstance(file_path, str):
            _delete(file_path)
        elif isinstance(file_path, list):
            for path in file_path:
                _delete(path)
        else:
            raise ValueError("路径只能为 str 或 list 类型 ！！！")

    def find_file(self, include_format=None, exclude_format=None, match=None):
        # type:(Optional[list,str], Optional[list,str], Optional[str])->Optional[List[str]]
        """

        Parameters
        ----------
        path 文件按路径
        include_format 可选，包括的文件类型，
        exclude_format 可选，不包括的文件类型
        match 可选，通过正则表达式匹配文件(路径匹配)

        Returns
        -------

        """
        files = []

        def find_file_path(path):  # type:(str)->None
            if os.path.isfile(path):
                suffix = path.split(".")[-1]
                if match is not None:
                    if len(re.compile(match).findall(path)) > 0:
                        files.append(path)
                        if (include_format and suffix not in include_format) or (
                                exclude_format and suffix in exclude_format):
                            files.remove(path)
                else:
                    if (include_format and suffix in include_format) or (
                            exclude_format and suffix not in exclude_format):
                        files.append(path)
            else:
                current_file_list = os.listdir(path)
                for file in current_file_list:
                    file_path = os.path.join(path, file)
                    find_file_path(path=file_path)

        if include_format is not None or exclude_format is not None or match is not None:
            if not isinstance(include_format, (str, list)) and not isinstance(
                    exclude_format, (str, list)) and not isinstance(match, str):
                raise ValueError("include_format 和 exclude_format 只能为 str 或 list 类型 , match 只能未str类型 ！！！")
            if isinstance(include_format, str):
                include_format = [include_format]
            if isinstance(exclude_format, str):
                exclude_format = [exclude_format]
            find_file_path(self.origin_path)

        if len(files) < 1:
            logging.warning("未找到任何满足条件的文件！！！")
        return files

    def remove(self, save_format=None, remove_format=None, match=None):
        # type:(Optional[list, str], Optional[list, str], Optional[str])->None
        """

        Parameters
        ----------
        path 文件路径
        save_format 除这些文件类型外的其他文件都删除，str或list
        remove_format 删除这些类型的文件，str或list
         match 可选，通过正则表达式匹配需要删除的文件

        Returns
        -------

        """
        if save_format is None and remove_format is None and match is None:
            files = [self.origin_path]
        else:
            files = self.find_file(include_format=remove_format, exclude_format=save_format, match=match)
        if len(files) > 0:
            file_process._delete_file(file_path=files)
        else:
            logging.warning("未删除任何文件！！！")

    def _copy_move(self, cp_metadata=True, include_format=None, exclude_format=None, match=None, is_cp=False):
        # type:(bool, Optional[list, str], Optional[list, str], Optional[str], bool)->None
        """

        Parameters
        ----------
        cp_metadata 可选，当为true时，复制文件时会复制文件的元数据，否则只会复制文件的权限
        include_format 可选，复制(移动)包括的文件类型
        exclude_format 可选，复制(移动)不包括的文件类型
        match 可选，通过正则表达式匹配需要复制(移动)的文件
        is_cp 可选，是否复制
        Returns
        -------

        """

        self._checkout_is_dir(self.target_path)
        if cp_metadata:
            copy_function = shutil.copy2
        else:
            copy_function = shutil.copy

        if include_format is None and exclude_format is None and match is None:
            files = [self.origin_path]
        else:
            files = self.find_file(include_format=include_format, exclude_format=exclude_format, match=match)
        if len(files) > 0:
            if is_cp:
                for file in files:
                    shutil.copytree(file, self.target_path, copy_function=copy_function)
            else:
                for file in files:
                    shutil.move(file, self.target_path, copy_function=copy_function)
        else:
            logging.warning("未操作任何文件！！！")

    def copy(self, cp_metadata=True, include_format=None, exclude_format=None, match=None):
        # type:(bool, Optional[list, str], Optional[list, str], Optional[str])->None
        """
        递归复制一个目录
        Parameters
        ----------
        cp_metadata 可选，当为true时，复制文件时会复制文件的元数据，否则只会复制文件的权限
        include_format 可选，复制(移动)包括的文件类型
        exclude_format 可选，复制(移动)不包括的文件类型
        match 可选，通过正则表达式匹配需要复制(移动)的文件

        Returns
        -------

        """
        self._copy_move(include_format=include_format, exclude_format=exclude_format,
                        cp_metadata=cp_metadata, match=match, is_cp=True)

    def move(self, cp_metadata=True, include_format=None, exclude_format=None, match=None):
        # type:(bool, Optional[list, str], Optional[list, str], Optional[str])->None
        """
        递归移动一个目录
        Parameters
        ----------
        path 文件路径
        save_format 除这些文件类型外的其他文件都移动，str或list
        remove_format 移动这些类型的文件，str或list
         match 可选，通过正则表达式匹配需要移动的文件

        Returns
        -------

        """
        self._copy_move(include_format=include_format, exclude_format=exclude_format,
                        cp_metadata=cp_metadata, match=match, is_cp=False)

# format = ['jpg', 'azw3', 'epub', 'mobi', 'pdf', 'docx']
# print(file_process(origin_path="D:\\0_AI\\myLearn\\Learn").find_file(exclude_format="md"))
# print(file_process(origin_path="D:\\0_AI\\myLearn\\Learn").find_file(include_format="md"))
# print(file_process(origin_path="D:\\0_AI\\myLearn\\Learn").find_file(match="README"))
# print(file_process(origin_path="D:\\0_AI\\myLearn\\Learn").find_file(include_format="md", match="README"))
# file_process(origin_path="D:\\0_AI\\myLearn\\exp", target_path="D:\\0_AI\\myLearn\\exp3").copy()
# file_process(origin_path="D:\\0_AI\\myLearn\\exp3\\f2", target_path="D:\\0_AI\\myLearn\\exp").move()
