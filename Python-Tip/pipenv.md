## Pipenv 是真的好用

### 1. 安装
```shell
pip install pipenv
```
### 2. 创建虚拟环境
```shell
$ cd myproject
$ pipenv install # 创建环境
$ pipenv install requests # 或者直接安装库
```
如果不存在pipfile,会生成一个pipfile，并且如果有的库添加会自动编辑该文件，不会我们手动更新requirements.txt文件了。

### 3.pipenv 切换国内源
* 阿里云：http://mirrors.aliyun.com/pypi/simple/
* 豆瓣：http://pypi.douban.com/simple/
* 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
* 中国科学技术大学：https://pypi.mirrors.ustc.edu.cn/simple/
