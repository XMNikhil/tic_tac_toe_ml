# main.py
from training import train_agent, test_agent

if __name__ == "__main__":
    print("Training the agent...")
    trained_agent = train_agent(episodes=10000)
    print("Training complete. Testing the agent...")
    test_agent(trained_agent)
