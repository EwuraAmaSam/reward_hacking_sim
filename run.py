# Quick gridworld test
from env.gridworld import GridWorld

# initialise a grid
env = GridWorld()
reset = env.reset()
done = False

actions = ['RIGHT', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT']

for a in actions:
    state, reward, done, info = env.step(a)
    print(f"Action {a}, State: {state}, Reward: {reward}, Done: {done}")