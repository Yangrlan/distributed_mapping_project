#!/usr/bin/env python
import rosbag
from rospy import Time

input_bag = "robot_Eric2.bag"
output_bag = "robot_Eric.bag"

# 定义话题映射关系（旧话题 -> 新话题）
topic_mapping = {
    "/Carol/velodyne_points": "/Eric/velodyne_points",
    "/Carol/imu/data": "/Eric/imu/data",
}

with rosbag.Bag(output_bag, 'w') as outbag:
    for topic, msg, t in rosbag.Bag(input_bag).read_messages():
        # 检查话题是否需要重映射
        new_topic = topic_mapping.get(topic, topic)  # 如果未映射，保留原名
        outbag.write(new_topic, msg, t)
