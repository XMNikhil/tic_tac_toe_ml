# agent.py
import random

class QLearningAgent:
    def __init__(self, player, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.player = player
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}
        self.actions = list(range(9))

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def set_q_value(self, state, action, value):
        self.q_table[(state, action)] = value

    def choose_action(self, state, available_actions):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_actions)
        q_values = [self.get_q_value(state, a) for a in available_actions]
        max_q = max(q_values)
        best_actions = [a for a in available_actions if self.get_q_value(state, a) == max_q]
        return random.choice(best_actions)

    def update_q_value(self, state, action, reward, next_state):
        max_next_q = max(self.get_q_value(next_state, a) for a in range(9))
        old_q = self.get_q_value(state, action)
        new_q = old_q + self.alpha * (reward + self.gamma * max_next_q - old_q)
        self.set_q_value(state, action, new_q)
