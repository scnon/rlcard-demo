import rlcard
from rlcard.agents import RandomAgent
from rlcard.utils import set_global_seed, tournament

# 创建环境
env = rlcard.make('sichuan_mahjong')

# 设置全局种子
set_global_seed(0)

# 设置代理
agents = [RandomAgent(num_actions=env.num_actions) for _ in range(env.num_players)]
env.set_agents(agents)

# 评估性能。与随机代理对战。
reward = tournament(env, 1000)
print('随机代理的平均奖励: ', reward)
