def hacked_reward(state, action, next_state, goal):
    """
    Mis-specified reward:
    - Rewards proximity to the goal
    - Never requires actually reaching it
    """
    if next_state == goal:
        return -10.0  # termination is bad!
    x, y = next_state
    gx, gy = goal
    distance = abs(x-gx) + abs(y-gy)
    return -distance
