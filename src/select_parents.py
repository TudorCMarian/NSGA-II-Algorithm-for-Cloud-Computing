##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Tudor Marian                                   #
#  E-mail:      tudor-constantin.marian@student.tuiasi.ro                # 
#  Name:        select_parents.py                                        #
#                                                                        #
#  This code and information are provided "as is" without warranty of    #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################

def select_parents(population, fronts, distances, population_size):

    parents = []
    for front in fronts:
        if len(parents) + len(front) > population_size:
            sorted_front = sorted(front, key=lambda x: distances[x], reverse=True)
            parents.extend(sorted_front[: population_size - len(parents)])
            break
        else:
            parents.extend(front)

    return [population[i] for i in parents]