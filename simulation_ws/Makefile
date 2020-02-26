ROS_ENV = install/setup.sh
GET_MARS_ENV = . $(ROS_ENV) && . install/mars/share/mars/launch/bucket.sh 
LAUNCH_MARS = $(GET_MARS_ENV) && roslaunch mars

EXCLUDE_PATTERN = \.swp|\.idea|__pycache__
build: log/setup $(shell find src -type f | grep -Ev '$(EXCLUDE_PATTERN)')
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
	$(LAUNCH_MARS) paused.launch

run-headless: build
	$(GET_MARS_ENV) && DISPLAY=:0 roslaunch mars headless.launch

run-full: build
	$(LAUNCH_MARS) mars_full_sim.launch

run-env: build
	$(LAUNCH_MARS) mars_env_only.launch

log/setup: setup.sh
	./setup.sh
	mkdir -p log
	touch log/setup

clean:
	rm -rf build/ bundle/ log/ install/

model-reset:
	rm -rf $$HOME/.ros/checkpoint
	. src/mars/launch/bucket.sh && \
		aws s3 rm s3://$$MODEL_S3_BUCKET/$$MODEL_S3_PREFIX/ --recursive
