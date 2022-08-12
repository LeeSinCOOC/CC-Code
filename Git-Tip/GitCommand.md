## Git 常用命令笔记

### 【GitBook服务多开】
```shell
gitbook build
gitbook serve --lrport 35730 --port 4001
```

### 【版本回退问题】
```shell
1.git checkout -- filename    放弃工作区的修改
2.git status 查看状态
3.git add   添加文件到暂存区
4.git commit filename -m 'message'    提交文件到库
5.git log   查看历史版本
6.git reflog    查看命令历史
7.git reset --soft HEAD^：将最近一次提交节点的提交记录回退到暂存区
8.git reset --mixed HEAD^：将最近一次提交节点的提交记录回退到工作区
9.git reset --hard HEAD^：将最近一次提交节点的提交记录全部清除
10.git reset --hard commitid:跳到指定的版本
```

+ 通过 `git checkout -- 文件名` 命令可以撤销文件在工作区的修改。

+ 通过 `git reset 文件名` 命令可以撤销指定文件的 `git add` 操作，即这个文件在暂存区的修改。

+ 通过 `git reset` 命令可以撤销之前的所有 `git add` 操作，即在暂存区的修改。

1. 修改后，文件没有放入暂存区（即文件一直在工作区）：用 `git checkout -- 文件名` 撤销工作区的改动（回到跟版本库一样的状态，即回到最近一次 git commit时的状态，所有改动全部清除）

2. 修改后，文件放入暂存区，且文件没有再次修改（即文件已经进入暂存区）：分两步：先用 `git reset <文件名>` 撤销 `git add` 操作（此时更改仍留在工作区），再执行 `git checkout -- 文件
名` 清除工作区的改动

3. 修改后，文件放入暂存区，且文件再次修改：分三步：先用 `git checkout -- 文件名` 撤销工作区的改动，再用 `git reset <文件名>` 撤销 `git add` 操作（此时更改仍留在工作区），最后执
行 `git checkout -- 文件名` 清除工作区的改动

### 【添加文件】
```shell
git add -A  添加所有变化
git add -u  添加被修改(modified)和被删除(deleted)文件，不包括新文件(new)
git add .   添加新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件
```

### 【删除文件】
+ 删除暂存区或分支上的文件, 同时工作区也不需要这个文件了
```shell
1 git rm file_path
2 git commit -m 'delete somefile'
3 git push
```

+ 需要删除暂存区或分支上的文件, 但本地又需要使用, 只是不希望这个文件被版本控制
```shell
git rm --cached file_path # 文件跟踪
git commit -m 'delete remote somefile'
git push
```

### 【git status 中文乱码】
```shell
git config --global core.quotepath false
```
