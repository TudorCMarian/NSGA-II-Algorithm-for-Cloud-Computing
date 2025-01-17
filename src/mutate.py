##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Tudor Marian                                   #
#  E-mail:      tudor-constantin.marian@student.tuiasi.ro                # 
#  Name:        mutate.py                                                #
#                                                                        #
#  This code and information are provided "as is" without warranty of    #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################
import random

def mutate(solution, bounds):
    """Apply mutation to a solution.
    Args:
        solution (list): Solution to mutate.
        bounds (list of tuples): [(min, max) for each dimension].
    """
    idx = random.randint(0, len(solution) - 1)
    solution[idx] = random.uniform(bounds[idx][0], bounds[idx][1])