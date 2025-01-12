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
import fast_nondominated_sort
import crowding_distance_assignment
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

if __name__ == "__main__":
    bounds = [(1,10), (1,10), (1,10)]
    parents = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 3, 4]]
    population_size = 50
    generations = 100
    crossover_prob = 0.9
    mutation_prob = 0.1

    population = initialize_population(population_size, bounds)

    for generation in range(generations):
        objectives = evaluate_population(population)
        fronts = fast_nondominated_sort.fast_nondominated_sort(objectives)
        parents = select_parents.select_parents(population, fronts, objectives, population_size)
        offspring = crossover(parents, crossover_prob, mutation_prob, bounds)
        population = parents + offspring
    
    objectives = evaluate_population(population)
    fronts = fast_nondominated_sort.fast_nondominated_sort(objectives)

    pareto_front = [objectives[i] for i in fronts[0]]
    plot_pareto_front(pareto_front)

    