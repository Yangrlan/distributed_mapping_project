#!/usr/bin/env python

import rosbag
import rospy
from rospy.rostime import Duration

def adjust_rosbag_timestamp(input_bag, output_bag, offset_seconds):
    offset = Duration.from_sec(offset_seconds)  # 5秒的偏移量

    with rosbag.Bag(output_bag, 'w') as outbag:
        for topic, msg, t in rosbag.Bag(input_bag).read_messages():
            # 调整时间戳
            new_time = t - offset
            outbag.write(topic, msg, new_time)

if __name__ == "__main__":
    input_bag = "robot_Carol2.bag"      # 原始 bag 文件
    output_bag = "robot_Carol.bag"    # 输出 bag 文件
    offset_seconds = 199.96           # 提前 5 秒

    adjust_rosbag_timestamp(input_bag, output_bag, offset_seconds)
    print(f"finshed adjusting timestamps and saved to {output_bag}!")
