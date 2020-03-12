#!/bin/bash
bundle=${1:-bundle/output.tar}
[ -f $bundle ] || { echo $bundle not found!; exit 1; }
s3keyhash="robomaker/sim-app/$(date | openssl sha1 | sed -E 's/^.*\s(.*)$/\1/').tar"
simapp_arn='arn:aws:robomaker:us-east-1:548134005492:simulation-application/randy-sim/1581925942372'

aws s3 cp $bundle s3://randy-rover/$s3keyhash
aws robomaker update-simulation-application --application $simapp_arn \
	--robot-software-suite name=ROS,version=Melodic \
	--simulation-software-suite name=Gazebo,version=9 \
	--rendering-engine name=OGRE,version=1.x \
	--sources s3Bucket=randy-rover,s3Key=$s3keyhash,architecture=X86_64
aws robomaker create-simulation-application-version --application $simapp_arn
