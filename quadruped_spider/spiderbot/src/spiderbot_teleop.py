#!/usr/bin/env python
import rospy
import math

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Control Your Robot Car
---------------------------
Moving around:
The control keys represents control of joint of robot for 8 DOF in orientation: 

q       w
   i  o
   j  k
a       s

q/w : movement of forward links - link 1
a/s : movement of rear links  - link 1

i/o : movement of forward links - link 0
j/k : movement of rear links  - link 0

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
    p = math.pi/6
    try:
        print (msg)
        while(1):
            key = getKey()
            if key == 'w':
                steer -= p
                pub_front_right_link1.publish(steer)
            elif key == 'q':
                steer -= p
                pub_front_left_link1.publish(steer)
            if key == 'a':
                steer -= p
                pub_rear_left_link1.publish(steer)
            elif key == 's':
                steer -= p
                pub_rear_right_link1.publish(steer)

            if key == 'o':
                steer += p
                pub_front_right_link0.publish(steer)
            elif key == 'i':
                steer += p
                pub_front_left_link0.publish(steer)
            if key == 'k':
                steer += p
                pub_rear_left_link0.publish(steer)
            elif key == 'l':
                steer += p
                pub_rear_right_link0.publish(steer)


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
            
            if key in ['q','a','w','s','u','i','j','k',' ']:
                print("steering angle: ", steer)

    except:
        print (e)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
