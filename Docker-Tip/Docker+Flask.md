## 从 Dockerfile 构建一个服务镜像
### Dockerfile
```dockerfile
FROM python:3.6
WORKDIR .

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD python3 app.py
#CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]
```

### 创建镜像：
```shell
sudo docker build -t 'testflask' .
sudo docker images
```

### 临时运行docker镜像：
```shell
sudo docker run -it --rm -p 80:80 testflask
```
  
### 生产环境运行(以daemon方式运行)
```shell
sudo docker run -d -p 80:80 --name test-flask-1 testflask
```


---
### requirements.txt
flask

---
### app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello docker&flask'

if __name__ == '__main__':
    app.run(host='0.0.0.0',
        port=5000,debug=True)
```
---
        
### gunicorn + gevent 
```shell
pip install gunicorn gevent
```
### gunicorn.conf.py
```python
workers = 5   
worker_class = "gevent"  
bind = "0.0.0.0:6009"
```
### CMD  
```shell
gunicorn [app文件名不带后缀]:app -c gunicorn.conf.py 
```
