# training.py
import random
from environment import TicTacToe
from agent import QLearningAgent

def train_agent(episodes):
    agent = QLearningAgent(player='X')
    for episode in range(episodes):
        env = TicTacToe()
        state = env.reset()
        done = False
        while not done:
            available_actions = env.available_actions()
            action = agent.choose_action(env.get_state(), available_actions)
            if env.take_action(action, 'X'):
                winner = env.check_winner()
                if winner is not None:
                    reward = 1 if winner == 'X' else -1 if winner == 'O' else 0
                    agent.update_q_value(env.get_state(), action, reward, env.get_state())
                    done = True
                    continue

            # Simulate opponent's move (random)
            if not done:
                opponent_action = random.choice(env.available_actions())
                env.take_action(opponent_action, 'O')
                winner = env.check_winner()
                if winner is not None:
                    reward = 1 if winner == 'X' else -1 if winner == 'O' else 0
                    agent.update_q_value(env.get_state(), action, reward, env.get_state())
                    done = True
    return agent

def test_agent(agent):
    env = TicTacToe()
    state = env.reset()
    done = False
    while not done:
        available_actions = env.available_actions()
        action = agent.choose_action(env.get_state(), available_actions)
        if env.take_action(action, 'X'):
            winner = env.check_winner()
            if winner is not None:
                print(f"Game over. Winner: {winner}")
                done = True
                continue

        # Simulate opponent's move (random)
        if not done:
            opponent_action = random.choice(env.available_actions())
            env.take_action(opponent_action, 'O')
            winner = env.check_winner()
            if winner is not None:
                print(f"Game over. Winner: {winner}")
