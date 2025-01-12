##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Tudor Marian                                   #
#  E-mail:      tudor-constantin.marian@student.tuiasi.ro                # 
#  Name:        plot_pareto_front.py                                     #
#                                                                        #
#  This code and information are provided "as is" without warranty of    #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################

import matplotlib.pyplot as plot

def plot_pareto_front(objectives):

    costs, times = zip(*objectives)
    plot.scatter(costs, times, color="blue", label="Solutions")
    plot.xlabel("Cost")
    plot.ylabel("Time")
    plot.title("Pareto Front")
    plot.legend()
    plot.show()