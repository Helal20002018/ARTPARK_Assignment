import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import rclpy.logging

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('publisher_node_1')
        self.publisher_ = self.create_publisher(String, 'robot_status', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Configure logging to exclude the timestamp
        rclpy.logging.set_logger_level(self.get_logger().name, rclpy.logging.LoggingSeverity.INFO)
        self.get_logger().info("Logging configured to exclude timestamp.")

    def timer_callback(self):
        msg = String()
        msg.data = 'Robot is running'
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()