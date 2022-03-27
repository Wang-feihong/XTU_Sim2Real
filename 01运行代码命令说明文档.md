# 运行代码命令说明文档

## 1 下载 docker image 
docker镜像地址：
```
xtulearner/rmus2022:my_tag
```
下载docker镜像:
```
docker pull xtulearner/rmus2022:my_tag
```
docker镜像token:
```
822f377a-7595-49b3-a608-5495eea1cb60
```
下载镜像至桌面，后续新建terminal相关操作均在桌面进行。<font color= Red>(标签为my_tag)</font>
![[rmus2022:my_tag.png]]
Access Token
![[token.png]]

## 2 docker server操作
### 2.1 打开docker container
查看sim2real_client ID
新建terminal,查看sim2real_server ID
``` 
sudo docker ps -a
```
![[ID.png]]
新建terminal,cd切换目录至目标文件夹ICRA-RM-Sim2Real/docker_server，打开sim2real_server容器,执行exec_server文件
```
cd ICRA-RM-Sim2Real/docker_server
```
```
./sudo docker start ID
```
```
./exec_server.sh 
```

运行ros
```
roscore
```

### 2.2 运行server环境
新建terminal，打开模拟器，显示rgb、depth、third_rgb画面
```
cd ICRA-RM-Sim2Real/docker_server
```
```
./exec_server.sh
```
```
cd ~/ros_x_habitat_ws/src/ros_x_habitat/
```
```
python3 src/scripts/roam_with_joy.py --hab-env-config-path ./configs/roam_configs/pointnav_rgbd_roam_mp3d_test_scenes.yaml
```
<font color= Red>如果出现错误，重启启动一次</font>

## 3 docker client操作
### 3.1 打开docker container
查看sim2real_client ID
新建terminal,查看sim2real_client ID
``` 
sudo docker ps -a
```

新建terminal,cd切换目录至目标文件夹ICRA-RM-Sim2Real/sim2real_client，打开sim2real_client容器,执行exec_server文件,可以选择打开ep_ws查看源代码
```
cd ./ICRA-RM-Sim2Real/docker_client
```
```
./sudo docker start ID
```
```
./exec_client.sh 
```
（选择性执行）
  ```
  code ~/ep_ws
  ```
  
### 3.2 运行client环境
新建terminal，打开可视化工具rviz,用于观察
```
cd ./ICRA-RM-Sim2Real/docker_client
```
```
./exec_client.sh 
```
```
roslaunch carto_navigation navigation.launch
```

### 3.3  运行自动导航程序
新建terminal，运行我们的定点导航程序
```
cd ./ICRA-RM-Sim2Real/docker_client
```
```
./exec_client.sh 
```
```
python3 ep_ws/src/sim2real_ep/fh_ws/scripts/c_flie.py
```

### 3.4 检测矿石
<font color= Red>等待小车自动导航到矿石前方，再运行检测程序</font>
新建terminal，检测矿石
```
roscd ep_detect_and_grasp
```
```
python3 detect_cube.py
```

### 3.5 抓取矿石
<font color= Red>等待小车自动导航到矿石前方，再运行抓取程序</font>
新建terminal，抓取矿石
输入以下命令：
```
roscd ep_detect_and_grasp
```

```
python3 grasp_cube.py
```
运行grasp_cube.py前请确保detect_cube.py已经运行

<font color= Red>** 目前我队进度只能使小车定点导航，然后根据组委会程序，开启目标检测及抓取1号矿石。很遗憾还没来得及实现小车后续的功能-_-,另外我们尝试制作.launch文件整合程序，一次将所有程序执行，但也是初学还未能实现。** </font>

