## Linux 系统使用中遇到的报错解决方式

## 【解决】E: 无法获取 dpkg 前端锁 (/var/lib/dpkg/lock-frontend)，是否有其他进程正占用它？
+ 网络方案：
```shell
1.ps -e|grep apt-get
2.sudo kill 6965
3.sudo rm /var/cache/apt/archives/lock  
4.sudo rm /var/lib/dpkg/lock
5.sudo apt-get update
```

+ 我的是18：
```shell
1.sudo rm /var/lib/dpkg/lock-frontend
```

###【文件名乱码问题】
```shell
sudo apt-get install convmv
convmv -f gbk -t utf-8 -r --notest /home/wwwroot
```

