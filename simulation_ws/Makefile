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
	. install/setup.sh && . install/mars/share/mars/launch/bucket.sh \
		&& roslaunch mars mars_full_sim.launch

clean:
	rm -rf build/ bundle/ log/ install/ deploy
