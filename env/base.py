from abc import ABC, abstractmethod

class Environment(ABC):
    """
    Abstract base class for all environments.

    This defines the contract between:
    - The world (environment)
    - The optimizer (agent)

    If this contract is mis-specified,
    the agent will optimize the wrong thing.
    """

    @abstractmethod
    def reset(self):
        """
        Resets the environment to an initial state.

        Returns:
            state: Any representation of the environment state
        """
        pass

# The fact that an agent receives a reward does not mean they acted as intended.
    @abstractmethod
    def step(self, action):
        """
        Applies an action to the environment.

        Args:
            action: A valid action for the environment

        Returns:
            next_state: The state after the action
            reward (float): The reward signal for this step
            done (bool): True if the episode is over
            info (dict): Optional debugging / interpretability info
        """
        pass
