。## Python pip 常用笔记

### 改延时，默认6000
```shell
pip --default-timeout=100 install packagename   
```
### 不使用缓存
```shell
pip  --no-cache-dir install packagename
```
### 报错
`【Can not perform a '--user' install. User site-packages are not visible in this virtualenv.】`
```shell
vim ~/.config/pip/pip.conf
user=false
```
### 临时用源
```shell 
pip install https://pypi.douban.com/simple/
```
* 阿里云 https://mirrors.aliyun.com/pypi/simple/
* 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
* 豆瓣(douban) http://pypi.douban.com/simple/
* 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
* 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
### 修改配置源
  * linux: `~/.pip/pip.conf`
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```  
  * windows:`C:\Users\xx\pip\pip.ini`
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
### 缓存位置
`~/.cache/pip`

### 下载whl包
```shell
pip download -r requirements.txt -d /mnt/data/ChenJian/XiaoLong_PigCount/pipwhl -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

### 安装whl包：
```shell
pip install -r pipwhl/*
```

### conda换源使用：
```shell
conda config --remove-key channels
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```
