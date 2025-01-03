import numpy as np
import random
import matplotlib.pyplot as plt

# Step 1: Define the problem (objectives)
def evaluate_solution(solution):
    """Evaluate objectives for a given solution.
    Args:
        solution (list): [CPU allocation, RAM allocation, Storage allocation]
    Returns:
        tuple: (cost, time) - values of the objectives
    """
    cpu, ram, storage = solution
    
    # Objective 1: Minimize cost (example: weighted sum of resources)
    cost = 0.5 * cpu + 0.3 * ram + 0.2 * storage

    # Objective 2: Minimize time (example: inversely proportional to allocated resources)
    time = 1 / (0.4 * cpu + 0.4 * ram + 0.2 * storage + 1e-6)  # Avoid division by zero

    return cost, time

# Step 2: Initialize population
def initialize_population(size, bounds):
    """Generate an initial population of solutions.
    Args:
        size (int): Number of individuals in the population.
        bounds (list of tuples): [(min, max) for each dimension]
    Returns:
        list: List of solutions.
    """
    population = []
    for _ in range(size):
        individual = [random.uniform(b[0], b[1]) for b in bounds]
        population.append(individual)
    return population

# Step 3: Evaluate population
def evaluate_population(population):
    """Evaluate all individuals in the population.
    Args:
        population (list): List of solutions.
    Returns:
        list: List of objective values for each solution.
    """
    return [evaluate_solution(individual) for individual in population]

# Step 4: Plot Pareto front
def plot_pareto_front(objectives):
    """Plot the Pareto front.
    Args:
        objectives (list): List of (cost, time) tuples.
    """
    costs, times = zip(*objectives)
    plt.scatter(costs, times, color="blue", label="Solutions")
    plt.xlabel("Cost")
    plt.ylabel("Time")
    plt.title("Pareto Front")
    plt.legend()
    plt.show()

# Main script
if __name__ == "__main__":
    # Define problem bounds (CPU, RAM, Storage: range 1-10 units)
    bounds = [(1, 10), (1, 10), (1, 10)]

    # Initialize population
    population_size = 50
    population = initialize_population(population_size, bounds)

    # Evaluate population
    objectives = evaluate_population(population)

    # Plot solutions (initial population)
    plot_pareto_front(objectives)
