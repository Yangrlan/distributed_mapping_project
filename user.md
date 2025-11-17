1. 拆分rosbag
rosbag filter S3E_Dormitory.bag test.bag "(topic == '/Bob/velodyne_points' or topic =='/Bob/imu/data') and (t.to_sec() < 1660986159.537000)"
2. 合并rosbag
python merge_bag.py -v five_robots.bag robot_Alpha.bag robot_Donald.bag 

