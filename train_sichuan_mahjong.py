import rlcard
from rlcard.agents import RandomAgent
from rlcard.utils import tournament, Logger
from rlcard.utils.utils import set_seed
from rlcard.agents.dqn_agent import DQNAgent
import os
import argparse
import sichuan_mahjong

def train(env, num_episodes, save_path):
    # 设置全局种子
    set_seed(0)

    # 设置DQN代理
    agent = DQNAgent(num_actions=env.num_actions)
    env.set_agents([agent] + [RandomAgent(num_actions=env.num_actions) for _ in range(env.num_players - 1)])

    # 训练模型
    for episode in range(num_episodes):
        trajectories, _ = env.run(is_training=True)
        for ts in trajectories[0]:
            agent.feed(ts)

        if episode % 100 == 0:
            print(f'Episode {episode} completed')

    # 保存模型
    agent.save(save_path)
    print(f'Model saved to {save_path}')

def predict(env, model_path):
    # 加载模型
    agent = DQNAgent(num_actions=env.num_actions)
    agent.load(model_path)
    env.set_agents([agent] + [RandomAgent(num_actions=env.num_actions) for _ in range(env.num_players - 1)])

    # 进行预测
    trajectories, _ = env.run(is_training=False)
    actions = [ts[1] for ts in trajectories[0]]
    print('Predicted actions:', actions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', action='store_true', help='Train the model')
    parser.add_argument('--predict', action='store_true', help='Predict using the trained model')
    parser.add_argument('--model_path', type=str, default='dqn_model', help='Path to save/load the model')
    parser.add_argument('--num_episodes', type=int, default=1000, help='Number of episodes for training')
    args = parser.parse_args()

    # 创建环境
    env = rlcard.make('sichuan_mahjong')

    if args.train:
        train(env, args.num_episodes, args.model_path)
    elif args.predict:
        predict(env, args.model_path)
    else:
        print('Please specify --train or --predict')
