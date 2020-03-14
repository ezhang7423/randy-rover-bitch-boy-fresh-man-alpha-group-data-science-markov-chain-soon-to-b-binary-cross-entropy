import importlib
import rl_coach.agents as agentmod
from rl_coach.core_types import TrainingSteps, EnvironmentEpisodes, EnvironmentSteps, RunPhase
from rl_coach.environments.gym_environment import GymVectorEnvironment
from rl_coach.base_parameters import VisualizationParameters, PresetValidationParameters, TaskParameters, Frameworks
from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.graph_managers.graph_manager import ScheduleParameters
from rl_coach.schedules import LinearSchedule
from rl_coach.exploration_policies.categorical import CategoricalParameters
from rl_coach.filters.filter import NoInputFilter, NoOutputFilter, InputFilter
from rl_coach.filters.observation.observation_stacking_filter import ObservationStackingFilter
from rl_coach.filters.observation.observation_to_uint8_filter import ObservationToUInt8Filter
from rl_coach.memories.memory import MemoryGranularity
from markov import environments
import os

####################
# Graph Scheduling #
####################
schedule_params = ScheduleParameters()
schedule_params.improve_steps = TrainingSteps(100000)  # Changing to 100K
schedule_params.steps_between_evaluation_periods = EnvironmentEpisodes(40)
schedule_params.evaluation_steps = EnvironmentEpisodes(5)
schedule_params.heatup_steps = EnvironmentSteps(0)

###############
# Environment #
###############
Training_Ground_Filter = InputFilter(is_a_reference_filter=True)


env_params = GymVectorEnvironment()
env_params.level = 'Mars-v1'


vis_params = VisualizationParameters()
vis_params.dump_csv = True
vis_params.dump_signals_to_csv_every_x_episodes = 1
vis_params.tensorboard = True

########
# Test #
########
preset_validation_params = PresetValidationParameters()
preset_validation_params.test = True
preset_validation_params.min_reward_threshold = 2000
preset_validation_params.max_episodes_to_achieve_reward = 1000

#########
# Agent #
#########
agents = {}
agent_path = agentmod.__path__[0]
for name in os.listdir(agent_path):
    if name.endswith(".py") and not name.startswith("__"):
        module = name[:-3]
        agents[module] = importlib.import_module(f'rl_coach.agents.{module}')

agent_list = [agents['clipped_ppo_agent'].ClippedPPOAgentParameters, agents['rainbow_dqn_agent'].RainbowDQNAgentParameters,
              # agents['acer_agent'].ACERAgentParameters,
              agents['qr_dqn_agent'].QuantileRegressionDQNAgentParameters,
              agents['categorical_dqn_agent'].CategoricalDQNAgentParameters, agents['ppo_agent'].PPOAgentParameters,
              agents['nec_agent'].NECAgentParameters, agents['dfp_agent'].DFPAgentParameters, agents['pal_agent'].PALAgentParameters,
              agents['actor_critic_agent'].ActorCriticAgentParameters, agents['mmc_agent'].MixedMonteCarloAgentParameters,
              agents['dqn_agent'].DQNAgentParameters, agents['ddqn_agent'].DDQNAgentParameters,
              agents['bootstrapped_dqn_agent'].BootstrappedDQNAgentParameters, agents['n_step_q_agent'].NStepQAgentParameters,
              agents['policy_gradients_agent'].PolicyGradientsAgentParameters]

agent_params = agent_list[int(os.getenv('COACH_ALGO', 0))]()

# Create graph manager
graph_manager = BasicRLGraphManager(agent_params=agent_params,
                                    env_params=env_params, schedule_params=schedule_params,
                                    vis_params=vis_params, preset_validation_params=preset_validation_params)
