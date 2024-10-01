from mdp import *
from utils import print_table
import sys

class MDPVacuumAgent:
    def __init__(self, environment, policy, battery_life=10, gamma = 0.9):
        self.environment = environment
        self.policy = policy
        self.current_state = (3,3)
        self.path = [self.current_state] 
        self.reward = 0
        self.battery_life = battery_life
        self.gamma = gamma 
    
    def update_gamma(self):
        """Dynamically update the discount factor gamma based on remaining battery life."""
        self.gamma = 1 - (1 / self.battery_life) if self.battery_life > 1 else 0.1
        print(f"Updated gamma to {self.gamma} based on remaining battery life: {self.battery_life}")

    def pickedAction(self, transition):
        weights = [weight[0] for weight in transition]
        states = [state[1] for state  in transition]
        return random.choices(population=states, weights=weights)

    def move(self):
        print(f"\n{self.current_state} is the start state. Starting vacuum!\n")
        while self.current_state not in environment.terminals:
            # update gamma before each move
            self.update_gamma()

            # get the recommended action given the state
            action = self.policy[self.current_state] 

            # randomly pick an action based on its weight
            self.current_state = self.pickedAction(self.environment.transitions[self.current_state][action])[0]
            
            # log its reward and print the resulting actions
            self.reward += self.environment.reward[self.current_state]
            self.battery_life -=1

            print(f"Vacuum moved from {self.path[-1]} to: {self.current_state}. " + 
                f"Reward Total: {'%.1f' % self.reward} ({'%.1f' % self.environment.reward[self.current_state]})")

            self.path.append(self.current_state)
        print(f"\n{self.current_state} is a terminal state. Stopping vacuum!\n")

if __name__ == "__main__":
    try:
        reward = float(sys.argv[1])
        if reward == 0:
            reward = 0.0000001
    except:
        print(f"Agrument: {sys.argv[1]} is not a float. Please input a value between -inf and inf.")
        quit()

    environment = GridMDP([[reward, reward, reward, reward],
                            [reward, None, reward, reward],
                            [reward, reward, reward, reward],
                            [reward, -1, reward, 10]],
                            terminals=[(1, 0), (3, 0)],
                            gamma = 0.9)

    # Get the policy iteratively using value_iteration given the environment
    pi = best_policy(environment, value_iteration(environment, 0.001))

    # Create the vacuum agent using the best policy
    vacuum_agent = MDPVacuumAgent(environment, pi, battery_life=10, gamma=0.9)
    vacuum_agent.move()

    print(f"Path followed by the vacuum agent: {vacuum_agent.path}\n")
    print_table(environment.to_arrows(pi))