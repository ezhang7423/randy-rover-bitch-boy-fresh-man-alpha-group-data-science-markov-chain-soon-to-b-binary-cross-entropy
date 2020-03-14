#!/bin/bash
if [ $# -eq 0 ]; then
    cat << EOM
Usage: ./scripts/test-algos.sh [algo1 [algo2...]], where algoN is:
0: clipped_ppo_agent.ClippedPPOAgentParameters
1: rainbow_dqn_agent.RainbowDQNAgentParameters,
2: qr_dqn_agent.QuantileRegressionDQNAgentParameters
3: acer_agent.ACERAgentParameters,
4: categorical_dqn_agent.CategoricalDQNAgentParameters
5: ppo_agent.PPOAgentParameters,
6: nec_agent.NECAgentParameters
7: dfp_agent.DFPAgentParameters
8: pal_agent.PALAgentParameters,
9: actor_critical_agent.ActorCriticAgentParameters
10: mmc_agent.MixedMonteCarloAgentParameters,
11: dqn_agent.DQNAgentParameters
12: ddqn_agent.DDQNAgentParameters,
13: bootstrapped_dqn_agent.BootstrappedDQNAgentParameters
14: n_step_q_agent.NStepQAgentParameters,
15: policy_gradients_agent.PolicyGradientsAgentParameters
EOM
    exit 1
fi
[ -z "$VIRTUAL_ENV" ] && { echo Must run from venv!; exit 2; }

export MODEL_S3_BUCKET="randy-rover"
export ROS_AWS_REGION="us-east-1"
export MARKOV_PRESET_FILE="algo_test.py"
[ -z "$DISPLAY" ] && export DISPLAY=:0

base_dir="$HOME/.ros/algo_test"
model_dir="$base_dir/models"
log_dir="$base_dir/logs"
preprefix="local/algo_test"
export MODEL_S3_PREFIX=$preprefix
export LOCAL_MODEL_DIRECTORY=$model_dir
export COACH_ALGO=0

cd "$(dirname $VIRTUAL_ENV)/simulation_ws"
make build
. install/setup.bash

for i in $@; do
    COACH_ALGO=$i
    MODEL_S3_PREFIX="$preprefix/$i"
    LOCAL_MODEL_DIRECTORY="$model_dir/$i"
    [ -d $LOCAL_MODEL_DIRECTORY ] || mkdir -p $LOCAL_MODEL_DIRECTORY
    [ -d $log_dir/$i ] || mkdir -p $log_dir/$i
    roslaunch mars headless.launch &> "$log_dir/$i/$(date -Iseconds).log" &
done
jobs -l
