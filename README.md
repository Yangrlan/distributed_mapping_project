# distributed_mapping_project

A repository for the distributed mapping of ground robots, including some dataset and onboard tests.

## 1. Prerequisited

### 1.1 Ubuntu and ROS

Ubuntu 20.04.  [ROS Installation](http://wiki.ros.org/ROS/Installation).

### 1.2 PCL && Eigen && OpenCV

PCL>=1.8, follow [PCL Installation](https://pointclouds.org/). 

Eigen>=3.3.4, follow [Eigen Installation](https://eigen.tuxfamily.org/index.php?title=Main_Page).

OpenCV>=4.2, follow [Opencv Installation](http://opencv.org/).
### 1.3 GTSAM

GTSAM 4.0.3, follow [GTSAM Installation](https://github.com/borglab/gtsam.git).

### 1.4 Livox SDK2 & livox_ros_driver2
Livox SDK2 & livox_ros_driver2, follow [Livox SDK2 Installation](https://github.com/Livox-SDK/Livox-SDK2.git)
 and [livox_ros_driver2 Installation](https://github.com/Livox-SDK/livox_ros_driver2.git).

## 2. Compilation

Create the source code folder and set up the configuration:

```
mkdir -p ~/cslam_ws/src
cd ~/cslam_ws
catkin init
catkin config --merge-devel
catkin config --cmake-args -DCMAKE_BUILD_TYPE=Release
```
Then clone and build:
```
cd src
git clone https://github.com/Yangrlan/distributed_mapping_project.git
wstool init
wstool merge ./distributed_mapping_project/DCL-SLAM/dependencies.rosinstall
wstool update
catkin build dcl_fast_lio
```

## 3. Test
Download the ROS bag containing the sensor data of five robots in [Five robots rosbag](https://huggingface.co/datasets/yangrlan/five_robots).
Then run the launch script:
```
source ./devel/setup.bash
roslaunch dcl_slam run_on_PC.launch
```
If you want to do onboard testing, edit the parameters `the number of robots` and `robotPrefix` in the file `run_onboard.launch`, then run the script on your onboard computer:
```
source ./devel/setup.bash
roslaunch dcl_slam run_onboard.launch
```
And remember to set up the multi-robot configuration of ROS before launching it!!! 
You can follow the instruction in [multi-robot configuration](https://blog.csdn.net/zhanghm1995/article/details/106781954).

## 4. Mapping Results

See the video files in this repository, including an onboard test of three robots and a dataset test of five robots.

## 5. Extra Bonus

The scripts and an easy-to-use instruction `user.md` to edit the ROS bags are also contained in this repository. Feel free to use it.

## 6. Acknowledgement
The repository is adapted from [DCL_SLAM](https://github.com/PengYu-Team/DCL-SLAM), thanks the authors for their great work.
Also thanks all the researchers participated in this project.
