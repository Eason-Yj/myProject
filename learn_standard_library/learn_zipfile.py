import zipfile  # 引入zip管理模块
import os
import logging


def file_to_zip(filepath, savepath):  # type:(str,str)->None
    """
    将文件或文件夹压缩为zip包
    :param filePath: 需要压缩的文件(文件夹)的路径
    :param savePath: 生成的zip包的保存路径,以.zip为结尾
    :return: 
    """

    def writeAllFileToZip(dir_path, zip_file, save_path='', zip_path=''):  # type:(str,zipfile.ZipFile,str,str)->None
        dir_list = []
        for child in os.listdir(dir_path):
            # 先压缩完当前层的所有文件
            absFile = os.path.join(dir_path, child)  # 子文件的绝对路径
            if absFile == save_path:
                continue

            if os.path.isfile(absFile):  # 判断是普通文件，直接写到zip文件中。
                zip_file_path = os.path.join(zip_path, child)
                print('zip_file_path', zip_file_path)
                zip_file.write(filename=absFile, arcname=zip_file_path)
            else:
                dir_list.append(child)

        if len(dir_list) > 0:
            print(dir_list)
            # 再深入下一层级目录继续压缩文件
            for child_dir in dir_list:
                zip_path = os.path.join(zip_path, child_dir)  # 改成相对路径，否则解压zip是/User/xxx开头的文件。
                absFile = os.path.join(dir_path, child_dir)  # 子文件的绝对路径
                zip_file.write(filename=absFile, arcname=zip_path)  # 在zip文件中创建文件夹
                writeAllFileToZip(dir_path=absFile, zip_path=zip_path, zip_file=zip_file)  # 递归操作

    if not os.path.exists(filepath):
        raise ValueError("Compressed file (folder) {} does not exist".format(filepath))
    save_dir = os.path.dirname(savepath)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 创建空的zip文件(ZipFile类型)。参数w表示写模式。zipfile.ZIP_DEFLATE表示需要压缩，文件会变小。ZIP_STORED是单纯的复制，文件大小没变。
    zip_file = zipfile.ZipFile(savepath, "w", zipfile.ZIP_DEFLATED)

    logging.info("start file compressed to zip format:")
    writeAllFileToZip(dir_path=filepath, zip_file=zip_file, save_path=savepath)
    logging.info("file compression succeeded: {}".format(savepath))


if __name__ == '__main__':
    file_path = ''
    save_path = ''
    file_to_zip(filepath=file_path, savepath=save_path)
