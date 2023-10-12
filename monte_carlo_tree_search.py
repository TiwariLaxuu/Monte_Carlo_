import random

#simple MCTS algorithm for a two-player game like Tic-Tac-Toe 
class Node:
    def __init__(self, state, parent=None):
        self.state = state  # The game state at this node
        self.parent = parent  # Parent node
        self.children = []  # Child nodes
        self.visits = 0  # Number of times this node has been visited
        self.value = 0  # Value associated with this node

def select(node):
    # Select a child node based on UCT (Upper Confidence Bound for Trees) formula
    exploration_weight = 1.0  # Adjust this value to balance exploration vs. exploitation
    return max(node.children, key=lambda child: child.value / (child.visits + 1e-6)
                                                + exploration_weight * (2 * (2 * node.visits + 1) / (child.visits + 1e-6))**0.5)

def expand(node):
    # Expand the node by adding all possible child states
    untried_actions = [action for action in node.state.get_legal_actions() if action not in [child.state.last_action for child in node.children]]
    if untried_actions:
        action = random.choice(untried_actions)
        new_state = node.state.perform_action(action)
        child_node = Node(new_state, parent=node)
        child_node.state.last_action = action
        node.children.append(child_node)
        return child_node
    else:
        return node  # No untried actions, return the node itself

def simulate(node):
    # Simulate a random game from this node and return the result
    return node.state.simulate_random_game()

def backpropagate(node, result):
    # Update the node's value and visit count and propagate the result up the tree
    while node is not None:
        node.visits += 1
        node.value += result
        node = node.parent

def monte_carlo_tree_search(initial_state, iterations):
    root = Node(initial_state)
    
    for _ in range(iterations):
        node = root
        while not node.state.is_terminal() and not node.children:
            node = expand(node)
        
        if node.children:
            node = select(node)
        
        result = simulate(node)
        backpropagate(node, result)
    
    # Choose the best action based on the most visited child
    best_child = max(root.children, key=lambda child: child.visits)
    best_action = best_child.state.last_action
    
    return best_action

# Example usage for Tic-Tac-Toe
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.last_action = None

    def get_legal_actions(self):
        return [i for i, val in enumerate(self.board) if val == ' ']

    def perform_action(self, action):
        new_state = TicTacToe()
        new_state.board = self.board.copy()
        new_state.board[action] = 'X' if not self.is_max_turn() else 'O'
        new_state.last_action = action
        return new_state

    def is_max_turn(self):
        return self.board.count('X') == self.board.count('O')

    def is_terminal(self):
        return self.board.count(' ') == 0 or self.get_winner() is not None

    def get_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]
        return None

    def simulate_random_game(self):
        state = self
        while not state.is_terminal():
            legal_actions = state.get_legal_actions()
            action = random.choice(legal_actions)
            state = state.perform_action(action)
        winner = state.get_winner()
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        else:
            return 0

# Usage
initial_state = TicTacToe()
best_action = monte_carlo_tree_search(initial_state, iterations=1000)
print("Best Action:", best_action)



#other example 
'''
classic optimization problem: the Traveling Salesman Problem (TSP). In this problem,
a salesperson must find the shortest route that visits a set of cities exactly 
once and returns to the starting city. We can use MCTS to approximate the 
solution.
'''
import random
import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_city):
        return math.sqrt((self.x - other_city.x) ** 2 + (self.y - other_city.y) ** 2)

class TSPState:
    def __init__(self, cities):
        self.cities = cities
        self.visited = [False] * len(cities)
        self.route = []
        self.total_distance = 0
        self.current_city = random.choice(cities)

    def get_legal_actions(self):
        return [i for i, visited in enumerate(self.visited) if not visited]

    def perform_action(self, action):
        new_state = TSPState(self.cities)
        new_state.visited = self.visited.copy()
        new_state.visited[action] = True
        new_state.route = self.route + [self.current_city]
        new_state.total_distance = self.total_distance + self.current_city.distance_to(self.cities[action])
        new_state.current_city = self.cities[action]
        return new_state

    def is_terminal(self):
        return all(self.visited)

    def get_cost(self):
        return self.total_distance

def monte_carlo_tree_search_tsp(initial_state, iterations):
    root = Node(initial_state)

    for _ in range(iterations):
        node = root
        while not node.state.is_terminal() and not node.children:
            node = expand(node)

        if node.children:
            node = select(node)

        result = simulate_tsp(node)
        backpropagate(node, result)

    # Find the best route based on the most visited child
    best_child = max(root.children, key=lambda child: child.visits)
    best_route = best_child.state.route + [best_child.state.current_city]
    return best_route

def simulate_tsp(node):
    return -node.state.get_cost()  # Minimize cost, so we use negative distance

# Create a list of cities (randomly generated in this example)
cities = [City(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(10)]

# Initialize the TSP state with the list of cities
initial_state = TSPState(cities)

# Example usage of MCTS to solve TSP
best_route = monte_carlo_tree_search_tsp(initial_state, iterations=1000)
print("Best Route:", best_route)
