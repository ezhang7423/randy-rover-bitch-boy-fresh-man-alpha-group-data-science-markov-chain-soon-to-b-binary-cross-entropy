#!/bin/bash
[ -f .catkin-workspace ] || { echo not in correct directory!; exit 1; }

colcon build
colcon bundle

../aws_scripts/update-sim-app.sh
../aws_scripts/create-sim-job.sh $1
