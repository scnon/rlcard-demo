import rlcard
from rlcard.agents import RandomAgent
from rlcard.utils import set_global_seed, tournament

# Make environment
env = rlcard.make('sichuan_mahjong')

# Set a global seed
set_global_seed(0)

# Set up agents
agents = [RandomAgent(num_actions=env.num_actions) for _ in range(env.num_players)]
env.set_agents(agents)

# Evaluate the performance. Play with random agents.
reward = tournament(env, 1000)
print('Average reward for RandomAgent: ', reward)
