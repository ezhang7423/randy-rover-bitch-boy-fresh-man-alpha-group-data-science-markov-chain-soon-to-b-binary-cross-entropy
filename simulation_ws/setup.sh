#!/bin/bash
if ! which roslaunch &> /dev/null; then
	sudo add-apt-repository universe multiverse restricted
	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
	sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
	sudo apt-get update
	sudo apt-get install ros-melodic-desktop-full
	sudo rosdep init
	echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
fi

rosdep update

sudo pip3 install -U awscli boto3
sudo pip3 install -U colcon-common-extensions colcon-ros-bundle
