cmake_minimum_required(VERSION 3.0.2)
project(user_ijnek)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
	rospy
	std_msgs
)

## catkin specific configuration
catkin_package(
	CATKIN_DEPENDS rospy std_msgs
)

## Include directories
include_directories(
	${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

## Install Python nodes
catkin_install_python(PROGRAMS
	scripts/talker.py
	scripts/listener.py
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Install launch files
install(DIRECTORY launch/
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
	FILES_MATCHING PATTERN "*.launch"
)

