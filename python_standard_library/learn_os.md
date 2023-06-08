# os 模块
## 创建文件夹
    os.mkdir(dir1_path)  # 单个文件夹创建
    os.makedirs(dir1_path)  # 递归创建多层文件夹

## 获取文件路径
    os.path.realpath(__file__)  # 获取指定文件的绝对路径,如果是软连接路径，则获取源文件路径
    os.path.abspath(__file__)  # 获取指定文件的绝对路径
    os.path.dirname(__file__)  # 获取文件(文件夹)所在目录
    os.path.getsize(__file__)  # 获取文件(文件夹)大小,单位为byte(字节=8bit)

## 判断路径
    os.path.isdir(path)  # 判断文件夹是否存在，返回True/False
    os.path.isfile(path)  # 判断文件是否存在，返回True/False
    os.path.isabs(__file__)  # 判断是否为绝对路径，返回True/False
    os.path.islink(__file__)  # 判断是否为链接（软硬），返回True/False
    os.path.ismount(__file__)  # 判断是否为挂载点，返回True/False
    os.path.samefile(file1_path, file1_path)  # 判断文件或文件夹是否相同，返回True/False

## 删除文件夹（文件）
    os.remove(file_path)  # 只能删除文件,无返回
    os.rmdir(dir_path)  # 删除文件夹，无返回
    os.unlink(file_path)  # 只能删除文件，有返回

    import shutil
    shutil.rmtree(dir_path) # 递归删除


## 获取文件信息
    os.path.getsize(file_path)  # 获取文件大小
