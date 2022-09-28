## Linux 常用命令笔记
### 没权限切换：
```shell
sudo -i
```
### kill所有python程序
```shell
pkill python
```
### 杀死所有进程除了1122 
```shell
killall5 -o 1122
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

### 查看内存：
```shell
watch -n 1 free -h 
```

### 清除内存：
```shell
echo 3 > /proc/sys/vm/drop_caches
```
