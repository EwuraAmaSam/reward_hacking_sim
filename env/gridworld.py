from env.base import Environment

class GridWorld(Environment):
    "Simple gridworld for the hacking simulation"

    def __init__(self, size=5, goal=(4,4), max_steps=50):
        self.size = size
        self.goal = goal
        self.max_steps = max_steps
        self.reset()

    # Reset agent to the original position
    def reset(self):
        self.agent_pos = (0,0)
        self.steps = 0
        return self.agent_pos
    
    # Define steps
    def step(self, action):
        """
        action: 'UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY'
        """
        x,y = self.agent_pos
        if action == 'UP':
            x = max(0, x-1)
        elif action == 'DOWN':
            x = min(self.size-1, x+1)
        elif action == 'LEFT':
            y = max(0, y-1)
        elif action == 'RIGHT':
            y = min(self.size-1, y+1)
        elif action == 'STAY':
            pass #no movement
        else:
            raise ValueError(f"Invalid action: {action}")
        
        self.agent_pos = (x,y)
        # Increase the number of steps
        self.steps += 1

        # Reward
        reward = 0.0
        done = self.agent_pos == self.goal or self.steps >= self.max_steps

        # Debugging info - to be added on hopefully
        info = {'step': self.steps}

        return self.agent_pos, reward, done, info



