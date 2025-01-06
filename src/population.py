##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Plosnita Eduard                                #
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

import random
from objectives import evaluate_solution

def initialize_population(size, bounds):
    return [[random.uniform(b[0], b[1]) for b in bounds] for _ in range(size)]

def evaluate_population(population):
    return [evaluate_solution(individual) for individual in population]
