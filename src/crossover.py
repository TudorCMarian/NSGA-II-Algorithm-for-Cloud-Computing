##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Tudor Marian                                   #
#  E-mail:      tudor-constantin.marian@student.tuiasi.ro                # 
#  Name:        crossover.py                                             #
#                                                                        #
#  This code and information are provided "as is" without warranty of    #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################

import mutate
import random

def crossover(parents, crossover_prob, mutation_prob, bounds):

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
