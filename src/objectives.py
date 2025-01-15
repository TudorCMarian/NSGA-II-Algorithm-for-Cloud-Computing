##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Plosnita Eduard                                #
#  E-mail:      eduard.plosnita@student.tuiasi.ro                        #
#  Name:        objectives.py                                            #
#                                                                        #
#  This code and information are provided "as is" without warranty of    #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################

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