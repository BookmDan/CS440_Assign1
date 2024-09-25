from mdp import *
from utils import print_table

class MDPVacuumAgent:
    def __init__(self, environment, policy):
        self.environment = environment
        self.policy = policy
        self.start_state = (3,3)
        self.current_state = self.start_state
        self.path = [self.current_state]  # To log the path followed
        self.reward = 0

    def transition(self, state, direction): # applies direction to current_index
        return [state[0] + direction[0], state[1] + direction[1]]

    def move(self):
        while self.current_state not in environment.terminals:
            action = self.policy[self.current_state]
            self.current_state = self.transition(self.current_state, action)
            self.path.append(self.current_state)
            print(f"Moved to: {self.current_state}")
        print("Terminal reached!")

    #def move(self):
    #    while self.current_state not in self.environment.terminals:  # Check if current state is a terminal state
    #        action = self.policy[self.current_state]
    #        transitions = environment.transitions[self.current_state][action]
    #        #curr_action = random.choices(transitions, weights=)
    #        new_state = self.transition(self.current_state, action)
    #        self.path.append(new_state)
    #        self.current_state = new_state
    #        #self.reward = environment.reward(self.current_state)
    #        print(f"Moved to: {self.current_state}")
#
    #    print("Terminal reached!")

# Example usage
if __name__ == "__main__":
    # Test environment from your setup


    REWARD = -0.4

    environment1 = GridMDP([[REWARD, REWARD, REWARD, REWARD],
                [REWARD, None, REWARD, REWARD],
                [REWARD, REWARD, REWARD, REWARD],
                [REWARD, -1, REWARD, 10]],
                terminals=[(1,0),(3,0)])

    REWARD1 = -20
    environment2 = GridMDP([[REWARD1, REWARD1, REWARD1, REWARD1],
                [REWARD1, None, REWARD1, REWARD1],
                [REWARD1, REWARD1, REWARD1, REWARD1],
                [REWARD1, -1, REWARD1, 10]],
                terminals=[(1,0),(3,0)])

    REWARD2 = 0
    environment3 = GridMDP([[REWARD2, REWARD2, REWARD2, REWARD2],
                [REWARD2, None, REWARD2, REWARD2],
                [REWARD2, REWARD2, REWARD2, REWARD2],
                [REWARD2, -1, REWARD2, 10]],
                terminals=[(1,0),(3,0)])

    REWARD3 = -2
    environment4 = GridMDP([[REWARD3, REWARD3, REWARD3, REWARD3],
                [REWARD3, None, REWARD3, REWARD3],
                [REWARD3, REWARD3, REWARD3, REWARD3],
                [REWARD3, -1, REWARD3, 10]],
                terminals=[(1,0),(3,0)])

    pi1 = best_policy(environment1, value_iteration(environment1, 0.001))
    print_table(environment1.to_arrows(pi1))
    print('\n')
    pi2 = best_policy(environment2, value_iteration(environment2, 0.001))
    print_table(environment2.to_arrows(pi2))
    print('\n')
    pi3 = best_policy(environment3, value_iteration(environment3, 0.001))
    print_table(environment3.to_arrows(pi3))
    print('\n')
    pi4 = best_policy(environment4, value_iteration(environment4, 0.001))
    print_table(environment4.to_arrows(pi4))

    # Solve the MDP with value iteration to get the best policy
    # pi = best_policy(environment, value_iteration(environment, 0.001))

    # Create the vacuum agent using the best policy
    vacuum_agent = MDPVacuumAgent(environment, pi)
    vacuum_agent.move()

    # Log the path followed
    print("Path followed by the vacuum agent:", vacuum_agent.path)