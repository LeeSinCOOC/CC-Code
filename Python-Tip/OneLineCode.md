# 一行代码的事
## 标准库
### 数值列表转字符串
```python
tring = ','.join(list(map(str,string_list)))
``` 
### tqdm 进度条
```python
from tqdm import tqdm
for i,j in enumerate(tqdm(a,desc='blue',colour='green')):
```

## 非标准库
### torch取值
```python
X = outputs.detach().cpu().numpy().tolist()
```

