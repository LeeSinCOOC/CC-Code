## Linux 常用命令笔记
### 没权限切换：
```shell
sudo -i
```
### kill所有python程序
```shell
pkill python
```

### 找文件：
```shell
find /home -name *init
```

### 查线程进程CPU参数
```shell
cat /proc/cpuinfo
```

### 查看物理cpu个数
```shell
grep 'physical id' /proc/cpuinfo | sort -u
```

### 查看核心数量
```shell
grep 'core id' /proc/cpuinfo | sort -u | wc -l
```

### 查看线程数
```shell
grep 'processor' /proc/cpuinfo | sort -u | wc -l
```

### GPU显存却被占用了很多
```shell
fuser -v /dev/nvidia*
```

### 查看文件大小
```shell
du -h coco/
```

### 查看磁盘使用情况
```shell
df -h
```

### tar压缩/解压
```shell
tar -cf xxx.tar x x
tar -xf xxx.tar
tar -tvf 列出文件
```

### 后台运行程序
```shell
nohup python command &
```

### 统计文件个数：
```shell
ls -l | grep "^-" | wc -l
```

### 计算文件大小：
```shell
du -h --max-depth=1
```

### 删除指定文件
```shell
find ./pigtrack/ -name "*.pyc" | xargs rm -rf
```

### 磁盘挂载：
1.查看新添加的盘符，可以在 root 下使用 `fdisk -l` 命令

2.格式化硬盘文件系统，`mkfs -t ext4 /dev/sde`

3.挂载硬盘，`mount /dev/sde /data`

4.开机自动挂载， `vim /etc/fstab`在最后面加入指定信息
```
UUID=67E91005-EB18-4E24-8410-EB9A1C2E3882 /data ext4 defaults 0 0
```
5.查看UUID
```
blkid -s UUID /dev/sdb
```

### 查看内存：
```shell
watch -n 1 free -h 
```

### 清除内存：
```shell
echo 3 > /proc/sys/vm/drop_caches
```

### [linux命令连接符区别]
;   分号，没有任何逻辑关系的连接符。当多个命令用分号连接时，各命令之间的执行成功与否彼此没有任何影响，都会一条一条执行下去。
||  逻辑或，当用此连接符连接多个命令时，前面的命令执行成功，则后面的命令不会执行。前面的命令执行失败，后面的命令才会执行。
&&  逻辑与，当用此连接符连接多个命令时，前面的命令执行成功，才会执行后面的命令，前面的命令执行失败，后面的命令不会执行，与 || 正好相反。
|   管道符，当用此连接符连接多个命令时，前面命令执行的正确输出，会交给后面的命令继续处理。若前面的命令执行失败，则会报错，若后面的命令无法处理前面命令的输出，也会报错。

### 写成脚本文件：
```
#!/bin/bash
sudo convmv -f gbk -t utf-8 -r --notest /tmp/OpenFile/
```
