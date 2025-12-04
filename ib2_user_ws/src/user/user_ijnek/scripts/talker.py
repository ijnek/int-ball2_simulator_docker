#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def main():
    rospy.init_node('sample_publisher', anonymous=False)
    rate_hz = rospy.get_param('~rate_hz', 5.0)

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(rate_hz)

    count = 0
    while not rospy.is_shutdown():
        msg = String(data=f"hello world {count}")
        pub.publish(msg)
        rospy.loginfo("Published: %s", msg.data)
        count += 1
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
