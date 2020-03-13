#!/bin/bash
[ -z "$VIRTUAL_ENV" ] && { echo Must run from venv! Create one in repo root and activate.; exit 2; }
if ! which roslaunch &> /dev/null; then
    sudo add-apt-repository universe multiverse restricted
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    sudo apt-get update
    sudo apt-get install ros-melodic-desktop-full
    sudo rosdep init
    echo "source /opt/ros/melodic/setup.bash" >> $HOME/.bashrc
    echo '##############################################'
    echo '##############################################'
    echo ROS installed! Source ~/.bashrc to get in PATH.
    echo '##############################################'
    echo '##############################################'

    pushd "$(dirname $VIRTUAL_ENV)/simulation_ws"
    rosdep install --from-paths src --ignore-src -r -y
    popd
fi
rosdep update

require_file="$(dirname $VIRTUAL_ENV)/simulation_ws/scripts/requirements.txt"
[ ! -f $require_file ] && { echo "Requirements not found! Is venv in repo root?"; exit 3; }
pip install -r $require_file
if ! pip list -l | grep 'python-apt' &> /dev/null; then # need python-apt hack
    pushd `mktemp -d`
    apt-get download python3-apt || exit 4
    dpkg -x python3-apt*.deb python3-apt
    cp -r python3-apt/usr/lib/python3/dist-packages/* $VIRTUAL_ENV/lib/python*/site-packages/
    popd
    pushd $VIRTUAL_ENV/lib/python*/site-packages
    mv apt_pkg.cpython*.so apt_pkg.so
    mv apt_inst.cpython*.so apt_inst.so
    popd
fi
