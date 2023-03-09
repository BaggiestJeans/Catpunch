import gym

env=gym.make("LunarLander-v2")
env.reset()
print("sample",env.action_space.sample())
print("ob space", env.observation_space.shape)
print("sam ob", env.observation_space.sample())

env.close()