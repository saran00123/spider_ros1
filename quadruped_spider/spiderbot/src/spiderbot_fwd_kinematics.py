#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Control Your Robot Car
---------------------------
Moving around:
        w
   a    s    d
        x

w/x : increase/decrease linear velocity 
a/d : increase/decrease angular velocity

space key, s : force stop

CTRL-C to quit
"""
e = """
Communications Failed
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot_teleop')

    pub_front_right_link1 = rospy.Publisher('/spiderbot/controller_front_right_link1/command', Float64, queue_size=10)
    pub_front_left_link1 = rospy.Publisher('/spiderbot/controller_front_left_link1/command', Float64, queue_size=10)
    pub_rear_left_link1 = rospy.Publisher('/spiderbot/controller_rear_left_link1/command', Float64, queue_size=10)
    pub_rear_right_link1 = rospy.Publisher('/spiderbot/controller_rear_right_link1/command', Float64, queue_size=10)
    pub_front_right_link0 = rospy.Publisher('/spiderbot/controller_front_right_link0/command', Float64, queue_size=10)
    pub_front_left_link0 = rospy.Publisher('/spiderbot/controller_front_left_link0/command', Float64, queue_size=10)
    pub_rear_left_link0 = rospy.Publisher('/spiderbot/controller_rear_left_link0/command', Float64, queue_size=10)
    pub_rear_right_link0 = rospy.Publisher('/spiderbot/controller_rear_right_link0/command', Float64, queue_size=10)

    steer = 0
    try:
        print (msg)
        while(1):
            key = getKey()
            if key == 'w':
                steer = 0.5236
                pub_front_right_link1.publish(steer)
                pub_front_left_link1.publish(steer)
                pub_rear_right_link1.publish(steer)
                pub_rear_left_link1.publish(steer)
            
            elif key == 's':
                steer = -0.5236
                pub_front_right_link1.publish(steer)
                pub_front_left_link1.publish(steer)
                pub_rear_right_link1.publish(steer)
                pub_rear_left_link1.publish(steer)

            elif key == 'a':
                steer = 0.5236
                pub_front_right_link0.publish(steer)
                pub_front_left_link0.publish(steer)
                pub_rear_right_link0.publish(steer)
                pub_rear_left_link0.publish(steer)
            elif key == 'd':

                steer = -0.5236
                pub_front_right_link0.publish(steer)
                pub_front_left_link0.publish(steer)
                pub_rear_right_link0.publish(steer)
                pub_rear_left_link0.publish(steer)


            elif key == ' ':
                steer = 0.0
                pub_front_right_link0.publish(steer)
                pub_front_left_link0.publish(steer)
                pub_rear_right_link0.publish(steer)
                pub_rear_left_link0.publish(steer)
                pub_front_right_link1.publish(steer)
                pub_front_left_link1.publish(steer)
                pub_rear_right_link1.publish(steer)
                pub_rear_left_link1.publish(steer)

            else:
                if (key == '\x03'):
                    break
            
            if key in ['w','a','s','d',' ']:
                print("steering angle: ", steer)

    except:
        print (e)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
