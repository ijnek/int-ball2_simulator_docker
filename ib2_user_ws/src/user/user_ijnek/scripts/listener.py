#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def _callback(msg: String):
    rospy.loginfo("Received: %s", msg.data)


def main():
    rospy.init_node('sample_subscriber', anonymous=False)
    rospy.Subscriber('chatter', String, _callback, queue_size=10)
    rospy.loginfo("Listener ready; waiting for messages on 'chatter'.")
    rospy.spin()


if __name__ == '__main__':
    main()
