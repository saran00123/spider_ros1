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

    p = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    try:
        print (msg)
        while(1):
            key = getKey()
            if key == 'w':
                p[0] += math.pi/150
                pub_front_right_link1.publish(p[0])
            elif key == 'q':
                p[1] += math.pi/150
                pub_front_left_link1.publish(p[1])
            if key == 'a':
                p[2] += math.pi/150
                pub_rear_left_link1.publish(p[2])
            elif key == 's':
                p[3] += math.pi/150
                pub_rear_right_link1.publish(p[3])

            if key == 'o':
                p[4] += math.pi/150
                pub_front_right_link0.publish(-(p[4]))
            elif key == 'i':
                p[5] += math.pi/150
                pub_front_left_link0.publish(p[5])
            if key == 'k':
                p[6] += math.pi/150
                pub_rear_left_link0.publish(-(p[6]))
            elif key == 'l':
                p[7] += math.pi/150
                pub_rear_right_link0.publish(p[7])


            elif key == ' ':
                p = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
                pub_front_right_link0.publish(p[0])
                pub_front_left_link0.publish(p[1])
                pub_rear_right_link0.publish(p[2])
                pub_rear_left_link0.publish(p[3])
                pub_front_right_link1.publish(p[4])
                pub_front_left_link1.publish(p[5])
                pub_rear_right_link1.publish(p[6])
                pub_rear_left_link1.publish(p[7])

            else:
                if (key == '\x03'):
                    break
            
            if key in ['q','a','w','s','u','i','j','k',' ']:
                print("steering angle: ", p)

    except:
        print (e)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
