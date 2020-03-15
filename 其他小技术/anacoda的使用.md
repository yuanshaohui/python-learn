# Anaconda的使用

----

## 介绍：

**anaconda**是一款python库的集合，里面有多种python库，并可以进行版本控制。

## 使用：

|                          命令                          |                功能                |
| :----------------------------------------------------: | :--------------------------------: |
| `conda create -n [创建环境的名字] python=[python版本]` |             创建新环境             |
|                    `conda env list`                    |           创建的环境列表           |
|            `conda remove --name test --all`            | 在环境内使用，删除该环境（待确定） |
|                  `activate python34`                   |              激活环境              |

- 环境总结：
  - `conda create --name python34 python=3.4`安装环境
  - `activate python34`激活环境
  - `source activate python34`(linux)激活环境
  - `python --version`检测是否已经切换成功环境
  - `deactivate python34`删除一个已有的环境
  - `source deactivate python34`(linux)删除一个已有的环境

- 安装/卸载第三方包
  - `conda install request`安装
  - `conda remove request`卸载
  - `conda list`查看安装的所有包

- 导入导出环境
  - `conda env export > environment.yaml`将包信息存入yaml文件中
  - `conda env create -f environment.yaml`需要使用这个虚拟环境时，导出