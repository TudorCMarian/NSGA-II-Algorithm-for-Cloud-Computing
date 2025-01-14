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

# Step 4: Fast Nondominated Sort
def fast_nondominated_sort(objectives):
    """Perform fast nondominated sorting.
    Args:
        objectives (list): List of (cost, time) tuples.
    Returns:
        list: A list of fronts, where each front is a list of indices.
    """
    S = [[] for _ in range(len(objectives))]
    front = [[]]
    n = [0] * len(objectives)
    rank = [0] * len(objectives)

    for p in range(len(objectives)):
        for q in range(len(objectives)):
            if dominates(objectives[p], objectives[q]):
                S[p].append(q)
            elif dominates(objectives[q], objectives[p]):
                n[p] += 1
        if n[p] == 0:
            rank[p] = 0
            front[0].append(p)

    i = 0
    while front[i]:
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i + 1
                    Q.append(q)
        i += 1
        front.append(Q)

    del front[-1]  # Remove the last empty front
    return front

def dominates(p, q):
    """Check if solution p dominates solution q.
    Args:
        p (tuple): Objectives of solution p.
        q (tuple): Objectives of solution q.
    Returns:
        bool: True if p dominates q, False otherwise.
    """
    return all(x <= y for x, y in zip(p, q)) and any(x < y for x, y in zip(p, q))

# Step 5: Crowding Distance Assignment
def crowding_distance_assignment(front, objectives):
    """Assign crowding distance to each solution in a front.
    Args:
        front (list): List of indices in the front.
        objectives (list): List of (cost, time) tuples.
    Returns:
        list: Crowding distances for each solution in the front.
    """
    distance = [0] * len(front)
    num_objectives = len(objectives[0])

    for m in range(num_objectives):
        sorted_front = sorted(front, key=lambda x: objectives[x][m])
        if len(sorted_front) == 0:
            return [0] * len(front)  # Fără distanțe calculate
        elif len(sorted_front) == 1:
            distance[sorted_front[0]] = float('inf')

        # distance[sorted_front[0]] = distance[sorted_front[-1]] = float('inf')
        for i in range(1, len(sorted_front) - 1):
            distance[sorted_front[i]] += (
                objectives[sorted_front[i + 1]][m] - objectives[sorted_front[i - 1]][m]
            ) / (max(o[m] for o in objectives) - min(o[m] for o in objectives) + 1e-6)

    return distance

# Step 6: Selection, Crossover, and Mutation
def select_parents(population, fronts, distances, population_size):
    """Select parents based on rank and crowding distance.
    Args:
        population (list): Current population.
        fronts (list): List of fronts.
        distances (list): List of crowding distances.
        population_size (int): Desired size of the population.
    Returns:
        list: Selected parents.
    """
    parents = []
    for front in fronts:
        if len(parents) + len(front) > population_size:
            sorted_front = sorted(front, key=lambda x: distances[x], reverse=True)
            parents.extend(sorted_front[: population_size - len(parents)])
            break
        else:
            parents.extend(front)

    return [population[i] for i in parents]

def crossover_and_mutation(parents, crossover_prob, mutation_prob, bounds):
    """Perform crossover and mutation to generate children.
    Args:
        parents (list): Selected parents.
        crossover_prob (float): Probability of crossover.
        mutation_prob (float): Probability of mutation.
        bounds (list of tuples): [(min, max) for each dimension].
    Returns:
        list: Children population.
    """
    children = []
    for _ in range(len(parents) // 2):
        if random.random() < crossover_prob:
            p1, p2 = random.sample(parents, 2)
            child1 = [(x + y) / 2 for x, y in zip(p1, p2)]
            child2 = [(x - y) / 2 for x, y in zip(p1, p2)]
        else:
            child1, child2 = random.sample(parents, 2)

        if random.random() < mutation_prob:
            mutate(child1, bounds)
        if random.random() < mutation_prob:
            mutate(child2, bounds)

        children.extend([child1, child2])

    return children

def mutate(solution, bounds):
    """Apply mutation to a solution.
    Args:
        solution (list): Solution to mutate.
        bounds (list of tuples): [(min, max) for each dimension].
    """
    idx = random.randint(0, len(solution) - 1)
    solution[idx] = random.uniform(bounds[idx][0], bounds[idx][1])


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

if __name__ == "__main__":

    #Input: Population
    population_size = 50
    problem_size = 3  # Number of decision variables (e.g., CPU, RAM, Storage)
    crossover_prob = 0.9
    mutation_prob = 0.1

    #Output: Children