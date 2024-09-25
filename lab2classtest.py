from mdp import *
from utils import print_table

class MDPVacuumAgent:
    def __init__(self, environment, policy):
        self.environment = environment
        self.policy = policy
        self.start_state = (3,3)
        self.current_state = self.start_state
        self.path = [self.current_state]  # To log the path followed
        self.recharge_station = (3,3)
        self.trap = (3,1)
        # self.reward = 0

    def transition(self, state, direction): # applies direction to current_index
        new_state = (state[0] + direction[0], state[1] + direction[1])
        if new_state in self.environment.terminals or self.environment.is_obstacle(new_state):
            print(f"Blocked moving to: {new_state}")
            return state  # Stay in the current state if moving to a trap or obstacle
        return new_state
    

    def move(self):
        recharge_station = (3,3)

        while self.current_state not in self.environment.terminals:  # Check if current state is a terminal state
            if self.current_state == recharge_station:
                print("Recharge station reached!")
                break

            action = self.policy(self.current_state)

            if action is None:
                print("No valid action found.")
                break

            next_state = self.transition(self.current_state, action)

            # If next state is a trap, find a valid path towards the recharge station
            if next_state == self.trap:
                print(f"Encountered trap at: {next_state}. Navigating towards recharge station.")
                self.navigate_to_recharge()
                break 
            
            self.current_state = self.transition(self.current_state, action)
            self.path.append(self.current_state)
            print(f"Moved to: {self.current_state}")

        print("Terminal reached!")
    
    def navigate_to_recharge(self):
        """Find a valid path to the recharge station while avoiding traps and obstacles."""
        while self.current_state != self.recharge_station:
            possible_moves = []
            for action in self.environment.actions:  # Loop through available actions
                new_state = self.transition(self.current_state, action)
                if new_state != self.current_state:  # Only consider valid moves
                    possible_moves.append(new_state)

            if not possible_moves:  # No valid moves
                print("No valid moves available to reach the recharge station.")
                break

            # Choose the best move towards the recharge station
            self.current_state = min(possible_moves, key=lambda s: self.distance(s, self.recharge_station))
            self.path.append(self.current_state)
            print(f"Navigated to: {self.current_state}")

    def distance(self, state_a, state_b):
        """Calculate Manhattan distance between two states."""
        return abs(state_a[0] - state_b[0]) + abs(state_a[1] - state_b[1])
    
    def is_obstacle(self, state):
        return self.grid[state[0]][state[1]] is None
           
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

    
    REWARD = 20
    environment = GridMDP([[REWARD, REWARD, REWARD, REWARD],
                            [REWARD, None, REWARD, REWARD],
                            [REWARD, REWARD, REWARD, REWARD],
                            [REWARD, -1, REWARD, 10]],
                            terminals=[(1, 0), (3, 0)])

    # Solve the MDP with value iteration to get the best policy
    pi = best_policy(environment, value_iteration(environment, 0.001))
    print(pi)

    # Create the vacuum agent using the best policy
    vacuum_agent = MDPVacuumAgent(environment, pi)
    print(pi[vacuum_agent.start_state])
    vacuum_agent.move()

    # Log the path followed
    print("Path followed by the vacuum agent:", vacuum_agent.path)