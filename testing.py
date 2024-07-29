# testing.py
from environment import TicTacToe
from agent import QLearningAgent

def play_game(agent1, agent2, verbose=False):
    env = TicTacToe()
    state = env.reset()
    done = False
    while not done:
        if env.get_state() == (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '):
            if verbose:
                print("Starting a new game.")
        
        available_actions = env.available_actions()
        
        # Agent 1's turn
        action = agent1.choose_action(env.get_state(), available_actions)
        if env.take_action(action, 'X'):
            if verbose:
                print(f"Agent 1 (X) takes action {action}")
                print_board(env.board)
            winner = env.check_winner()
            if winner:
                if verbose:
                    print(f"Game over. Winner: {winner}")
                return winner
        
        # Agent 2's turn
        if not done:
            action = agent2.choose_action(env.get_state(), available_actions)
            env.take_action(action, 'O')
            if verbose:
                print(f"Agent 2 (O) takes action {action}")
                print_board(env.board)
            winner = env.check_winner()
            if winner:
                if verbose:
                    print(f"Game over. Winner: {winner}")
                return winner

    if verbose:
        print("Game over. It's a draw.")
    return 'Draw'

def print_board(board):
    """Utility function to print the board."""
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        print("-" * 5)

def evaluate_agents(agent, num_games=100):
    agent2 = QLearningAgent(player='O')  # Create a second agent (could be random or another trained agent)
    agent2.epsilon = 0  # Set epsilon to 0 for deterministic moves in agent2

    results = {'X': 0, 'O': 0, 'Draw': 0}

    for _ in range(num_games):
        result = play_game(agent, agent2)
        results[result] += 1

    print(f"Evaluation Results after {num_games} games:")
    print(f"Agent X wins: {results['X']}")
    print(f"Agent O wins: {results['O']}")
    print(f"Draws: {results['Draw']}")
