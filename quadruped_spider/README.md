# ENPM662-Project2-Quadruped_Spiderbot
Modelling, Fwd, Inv Kinematics of a Quadruped Spider Robot

## Instructions to run the project:

* Download all the files in the package 
* Change the directory to catkin workspace using "cd ~/aditya97_satish_catkin_ws
* Ensure to source the aditya97_satish_catkin_ws prior to building the workspace
* Run catkin_make clean && catkin_make
* If some of the packages couldn't build, make sure to download the deependencies such as ros controllers from their website. 
* After successful cmake, now launch the project using
        
         roslaunch spiderbot spiderbot world.launch

* To run the teleop:
	Open a new terminal and run:

		rosrun spiderbot spiderbot_teleop.py

	
    ### The Keys are:
		
The control keys represents control of joint of robot for 8 DOF in orientation: 

q&emsp;&emsp; w<br>
&emsp;i&emsp;o<br>
&emsp;j&emsp;k<br>
a&emsp;&emsp; s<br>

q/w : movement of forward links - link 1
a/s : movement of rear links  - link 1

i/o : movement of forward links - link 0
j/k : movement of rear links  - link 0

space key, s : force stop

CTRL-C to quit

	
* To run forward kinematics validation:
	
		rosrun spiderbot_fwd_kinematics.py

### The workspace study and inverse kinematics joint angles plots and Simulation are added in the Drive Link. 
Link - https://drive.google.com/drive/folders/19MLxybskd75QSh_gTdxyU184A0bkAgcp?usp=share_link
#### Required packages are: 
* Python 3
* matplotlib and 
* math library 

Authors - 
- Aditya Chaugule (aditya97@umd.edu)
- Satish Vennapu (satish@2umd.edu)
