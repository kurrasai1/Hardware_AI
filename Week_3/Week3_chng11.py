import gym
import cupy as cp
import numpy as np  # still needed for Gym outputs
import time

# Initialize environment
env = gym.make('FrozenLake-v1', is_slippery=False)
state_space = env.observation_space.n
action_space = env.action_space.n

# Initialize Q-table on GPU
Q = cp.zeros((state_space, action_space))

# Hyperparameters
alpha = 0.8         # learning rate
gamma = 0.95        # discount factor
epsilon = 0.1       # exploration rate
episodes = 10000

# Start benchmarking
start_time = time.time()

for episode in range(episodes):
    state = env.reset()
    done = False

    while not done:
        # Choose action (epsilon-greedy)
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = int(cp.argmax(Q[state, :]))

        next_state, reward, done, _, _ = env.step(action)

        # Q-Learning update (GPU-based)
        old_value = Q[state, action]
        next_max = cp.max(Q[next_state, :])
        Q[state, action] = old_value + alpha * (reward + gamma * next_max - old_value)

        state = next_state

end_time = time.time()

# Print execution time and Q-table
print(f"Training completed in {end_time - start_time:.2f} seconds.")
print("\nFinal Q-table (rounded):")
print(cp.round(Q, 2).get())  # .get() moves data from GPU to CPU for display

