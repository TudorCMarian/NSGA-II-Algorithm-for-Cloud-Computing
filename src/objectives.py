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

def evaluate_solution(solution):
    
    cpu, ram, storage = solution
    cost = 0.5 * cpu + 0.3 * ram + 0.2 * storage
    time = 1 / (0.4 * cpu + 0.4 * ram + 0.2 * storage + 1e-6)
    return cost, time
