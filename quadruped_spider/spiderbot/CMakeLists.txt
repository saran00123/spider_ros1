cmake_minimum_required(VERSION 3.10.2)

project(spiderbot)

find_package(catkin REQUIRED)

catkin_package()
catkin_package()
catkin_install_python(PROGRAMS src/spiderbot_teleop.py src/spiderbot_fwd_kinematics.py
 DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
