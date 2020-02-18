build: $(shell find src -type f)
	colcon build
	touch build

bundle: build
	colcon bundle
	touch bundle

deploy: bundle
	./aws_scripts/update-sim-app.sh
	./aws_scripts/create-sim-job.sh
	touch deploy

run: build
	echo roslaunch
	. install/setup.sh
	roslaunch mars mars_full_sim.launch

clean:
	rm -rf build/ bundle/ log/ install/ deploy
