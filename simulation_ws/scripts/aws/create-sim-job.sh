#!/bin/bash
max_duration_sec=${1:-3600}
model_s3_prefix=robomaker
simapp_arn='arn:aws:robomaker:us-east-1:548134005492:simulation-application/randy-sim/1581925942372'

vars1="MARKOV_PRESET_FILE=mars_presets.py,MODEL_S3_BUCKET=randy-rover"
vars2="MODEL_S3_PREFIX=$model_s3_prefix,ROS_AWS_REGION=us-east-1"
env_vars="environmentVariables={$vars1,$vars2}"
package_config="packageName=mars,launchFile=mars_full_sim.launch"
vpc_conf='subnets=subnet-f4f825b9,subnet-7cc4cc52,securityGroups=sg-887f45dd,assignPublicIp=true'

aws robomaker create-simulation-job --max-job-duration-in-seconds $max_duration_sec \
	--iam-role arn:aws:iam::548134005492:role/simjobrole \
	--output-location s3Bucket=randy-rover,s3Prefix=robomaker/sim-out \
	--failure-behavior Continue --vpc-config $vpc_conf \
	--simulation-applications application=$simapp_arn,launchConfig="{$package_config,$env_vars}"
