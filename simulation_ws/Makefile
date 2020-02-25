GET_ENV = . install/setup.sh && . install/mars/share/mars/launch/bucket.sh 

build: log/setup $(shell find src -type f)
	colcon build
	touch build

bundle: build
	colcon bundle
	touch bundle

bundle/deploy: bundle
	./aws_scripts/update-sim-app.sh
	./aws_scripts/create-sim-job.sh
	touch bundle/deploy

deploy: bundle/deploy

run-paused: build
	$(GET_ENV) && roslaunch mars paused.launch

run-headless: build
	$(GET_ENV) && DISPLAY=:0 roslaunch mars headless.launch

run-full: build
	$(GET_ENV) && roslaunch mars mars_full_sim.launch

run-env: build
	$(GET_ENV) && roslaunch mars mars_env_only.launch

log/setup: setup.sh
	./setup.sh
	mkdir log
	touch log/setup
	echo ROS and tools installed! Source ~/.bashrc to get in PATH.

clean:
	rm -rf build/ bundle/ log/ install/

model-reset:
	rm -rf $$HOME/.ros/checkpoint
	. src/mars/launch/bucket.sh && \
		aws s3 rm s3://$$MODEL_S3_BUCKET/$$MODEL_S3_PREFIX/ --recursive
