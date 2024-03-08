#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import random
class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_gazebo')
        self.laser_sub_ = self.create_subscription(LaserScan, "/scan",self.subscriber_callback, 10)
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/cmd_vel", 10)
        # self.timer_ = self.create_timer(0.5, self.move_callback)

        self.get_logger().info("Node to Map Turtlebot House Started")
        self.speed = 0.2
        self.turn_speed = 0.5

    def generate_random_number(self):
     num = 0
     while num == 0:
        num = random.randint(-5, 5)


     return float(num)


    def subscriber_callback(self, msg):
        # Process scan data and decide on actions
        is_obstacle_in_front = min(min(msg.ranges[0:10]), min(msg.ranges[-10:])) < 0.6

        twist = Twist()

        if is_obstacle_in_front:
            twist.linear.x = 0.0
            twist.angular.z = self.generate_random_number()
        else:
            twist.linear.x = self.speed
            twist.angular.z = 0.0

        self.cmd_vel_pub_.publish(twist)
        


def main(args=None):
    rclpy.init(args=args)
    controller_node = ControllerNode()
    rclpy.spin(controller_node)
    controller_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
