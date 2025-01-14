##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Tudor Marian, Plosnita Eduard, Paul Aflorei    #
#  E-mail:      tudor-constantin.marian@student.tuiasi.ro                # 
#               eduard.plosnita@student.tuiasi.ro                        #
#               paul-bogdan.aflorei@student.tuiasi.ro                    #
#  Description: Resource Optimization in Cloud Computing Using NSGA-II   #
#                                                                        #
#  This code and information are provided "as is" without warranty of    #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################
import objectives
from population import initialize_population, evaluate_population
from crossover import crossover
import mutate
import select_parents
from fast_nondominated_sort import fast_nondominated_sort
from crowding_distance_assignment import crowding_distance_assignment
import matplotlib.pyplot as plt

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

# if __name__ == "__main__":
#     #ProblemSize => Curs
#     bounds = [(1,10), (1,10), (1,10)]

#     parents = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 3, 4]]
#     population_size = 50
#     generations = 100
#     crossover_prob = 0.9
#     mutation_prob = 0.1

#     population = initialize_population(population_size, bounds)

#     for generation in range(generations):
#         #EvaluateAgainstsObjectivesFunctions
#         objectives = evaluate_population(population)
#         #FastNondominatedSort
#         fronts = fast_nondominated_sort.fast_nondominated_sort(objectives)
#         #SelectParentByRank
#         parents = select_parents.select_parents(population, fronts, objectives, population_size)
#         #CrossoverAndMutation
#         offspring = crossover(parents, crossover_prob, mutation_prob, bounds)
#         #Merge(Population, Children)
#         population = parents + offspring
    
#     #EvaluateAgainstCondition
#     objectives = evaluate_population(population)

#     fronts = fast_nondominated_sort.fast_nondominated_sort(objectives)

#     pareto_front = [objectives[i] for i in fronts[0]]
#     plot_pareto_front(pareto_front)


if __name__ == "__main__":
    # Input parameters
    population_size = 50
    problem_size = 3  # Number of decision variables (e.g., CPU, RAM, Storage)
    crossover_prob = 0.9
    mutation_prob = 0.1
    generations = 100
    bounds = [(1, 10), (1, 10), (1, 10)]
    objectives = [[1, 3], [2, 2], [3, 1], [1.5, 2.5]]

    # Step 1: Initialize population
    population = initialize_population(population_size, bounds)

    # Step 2: Evaluate objectives for initial population
    objectives = evaluate_population(population)

    # Step 3: Perform fast non-dominated sort
    fronts = fast_nondominated_sort(objectives)
    print(f"Fronts: {fronts}")


    # Step 4: Start evolutionary process
    for generation in range(generations):
        # Assign crowding distances
        distances = crowding_distance_assignment(fronts, objectives)

        # Select parents
        parents = select_parents(population, fronts, distances, population_size)

        # Generate offspring through crossover and mutation
        offspring = crossover_and_mutation(parents, crossover_prob, mutation_prob, bounds)

        # Evaluate objectives for offspring
        offspring_objectives = evaluate_population(offspring)

        # Merge population and offspring
        population += offspring
        objectives += offspring_objectives

        # Perform fast non-dominated sort on the combined population
        fronts = fast_nondominated_sort(objectives)

        # Reduce population size to original size using ranking and crowding distance
        new_population = []
        new_objectives = []
        for front in fronts:
            if len(new_population) + len(front) > population_size:
                # Sort by crowding distance within the front
                sorted_front = sorted(front, key=lambda x: distances[x], reverse=True)
                remaining = population_size - len(new_population)
                new_population.extend([population[i] for i in sorted_front[:remaining]])
                new_objectives.extend([objectives[i] for i in sorted_front[:remaining]])
                break
            else:
                new_population.extend([population[i] for i in front])
                new_objectives.extend([objectives[i] for i in front])

        population = new_population
        objectives = new_objectives

    # Step 5: Extract Pareto front from the final population
    pareto_front = [objectives[i] for i in fronts[0]]

    # Plot Pareto front
    plot_pareto_front(pareto_front)