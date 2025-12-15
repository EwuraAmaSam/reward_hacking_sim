class GreedyAgent:
    """
    A simple agent that chooses the action
    that maximizes immediate reward.
    """
    def __init__(self, actions):
        self.actions = actions

    def choose_action(self, env):
         """
        Chooses the best action by simulating
        one step ahead for each possible action.
        """
         best_action = None
         best_reward = float('-inf')

        #  Save environment state
         original_pos = env.agent_pos
         original_steps = env.steps

         for action in self.actions:
             next_state, reward, done, info = env.step(action)

            #  Restore environment state
             env.agent_pos = original_pos
             env.steps = original_steps

             if reward > best_reward:
                 best_reward = reward
                 best_action = action
        
         return best_action

         

    