def intended_reward(state, action, next_state, goal):
    """
    Intended behavior:
    - Strong positive reward for reaching the goal
    - Small penalty per step to encourage efficiency
    """
    if next_state == goal:
        reward = 10.0

    x, y = next_state
    gx, gy = goal
    distance = abs(x - gx) + abs(y - gy)

    return -0.1 * distance


