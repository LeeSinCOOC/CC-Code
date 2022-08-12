## Screen 使用笔记

### Screen命令使用：
| 命令            |   描述              |
|----------------|--------------------|
| screen -S name |  打开新窗口          |
|screen -r name  |  重现窗口            |
|screen -ls      | 列出当前所有的session |
|screen -d name  | 远程detach某个session|
|screen -wipe    | 清除该会话           |

### 【screen相关】
+ 如何kill掉一个screen：  
```shell
screen -S session_name -X quit
```

+ 创建新screen:
```shell
screen -S yourname 
```  

+ 退出：
```shell
ctrl + a ---> ctrl + d
```  

+ 列出：
```shell
screen -ls
```  

+ 回会话：
```shell
screen -r yourname
```  
