# # Quick gridworld test
# from env.gridworld import GridWorld

# # initialise a grid
# env = GridWorld()
# reset = env.reset()
# done = False

# actions = ['RIGHT', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT']
# print("GRIDWORLD TEST")

# for a in actions:
#     state, reward, done, info = env.step(a)
#     print(f"Action {a}, State: {state}, Reward: {reward}, Done: {done}")



# print("REWARD TYPES TEST")

# from env.gridworld import GridWorld
# from rewards.intended import intended_reward
# from rewards.hacked import hacked_reward

# print("=== Intended Reward ===")
# env = GridWorld(reward_fn=intended_reward)
# state = env.reset()

# for _ in range(20):
#     state, reward, done, info = env.step('RIGHT')
#     print(state, reward)
#     if done:
#         break

# print("\n=== Hacked Reward ===")
# env = GridWorld(reward_fn=hacked_reward)
# state = env.reset()

# for _ in range(20):
#     state, reward, done, info = env.step('RIGHT')
#     print(state, reward)

from env.gridworld import GridWorld
from rewards.intended import intended_reward
from rewards.hacked import hacked_reward
from agent.agent import GreedyAgent

ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY']

def run_episode(env, agent, max_steps=20):
    state = env.reset()

    for _ in range(max_steps):
        action = agent.choose_action(env)
        state, reward, done, info = env.step(action)
        print(f"Action: {action}, State: {state}, Reward: {reward}")

        if done:
            print("Episode finished.")
            break

print("=== Intended Reward ===")
env = GridWorld(reward_fn=intended_reward)
agent = GreedyAgent(ACTIONS)
run_episode(env, agent)

print("\n=== Hacked Reward ===")
env = GridWorld(reward_fn=hacked_reward)
agent = GreedyAgent(ACTIONS)
run_episode(env, agent)

