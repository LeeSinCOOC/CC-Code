## Nginx 配置笔记
###【搭建文件服务器】
1.自己配置的文件存放在conf.d

2.配置文件如下
```
server {
    listen  0.0.0.0:5000;
    charset gbk,utf-8; # 避免中文乱码，注意顺序
    root /tmp/OpenFile;
    location / {
        autoindex on; # 索引
        autoindex_exact_size off; # 显示文件大小
        autoindex_localtime on; # 显示文件时间
    }
}
```

2.做完需要删除默认`sites-enabled`下的默认文件
