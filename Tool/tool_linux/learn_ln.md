# Linux ln（软连接和硬连接） 指令

## ln [选项] 源文件绝对路径 目标文件

- -s：建立软链接文件。如果不加 "-s" 选项，则建立硬链接文件；
- -f：强制。如果目标文件已经存在，则删除目标文件后再建立链接文件；

## 软连接和硬连接的区别：

- 硬连接：
    - 不论是修改源文件（test 文件），还是修改硬链接文件（test-hard 文件），另一个文件中的数据都会发生改变。
    - 不论是删除源文件，还是删除硬链接文件，只要还有一个文件存在，这个文件（inode 号是 262147 的文件）都可以被访问。
    - 硬链接不会建立新的 inode 信息，也不会更改 inode 的总数。
    - 硬链接不能跨文件系统（分区）建立，因为在不同的文件系统中，inode 号是重新计算的。
    - 硬链接不能链接目录，因为如果给目录建立硬链接，那么不仅目录本身需要重新建立，目录下所有的子文件，包括子目录中的所有子文件都需要建立硬链接，这对当前的
      Linux 来讲过于复杂。

- 软连接：
    - 不论是修改源文件（check），还是修改硬链接文件（check-soft)，另一个文件中的数据都会发生改变。
    - 删除软链接文件，源文件不受影响。而删除原文件，软链接文件将找不到实际的数据，从而显示文件不存在。
    - 软链接会新建自己的 inode 信息和 block，只是在 block 中不存储实际文件数据，而存储的是源文件的文件名及 inode 号。
    - 软链接可以链接目录。
    - 软链接可以跨分区。