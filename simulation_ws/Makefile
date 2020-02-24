GET_ENV = . install/setup.sh && . install/mars/share/mars/launch/bucket.sh 

build: $(shell find src -type f)
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

run-full: build
	$(GET_ENV) && roslaunch mars mars_full_sim.launch

run-env: build
	$(GET_ENV) && roslaunch mars mars_env_only.launch

clean:
	rm -rf build/ bundle/ log/ install/
