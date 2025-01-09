##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Paul Aflorei                                   #
#  E-mail:      paul-bogdan.aflorei@student.tuiasi.ro                    #
#  Description: Resource Optimization in Cloud Computing Using NSGA-II   #
#                                                                        #
#  This code and information are provided "as is" without warranty of    #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################


def crowding_distance_assignment(front, objectives):
    distance = [0] * len(front)
    num_objectives = len(objectives[0])

    for m in range(num_objectives):
        sorted_front = sorted(front, key=lambda x: objectives[x][m])
        if len(sorted_front) == 0:
            return [0] * len(front)
        elif len(sorted_front) == 1:
            distance[sorted_front[0]] = float('inf')

        # distance[sorted_front[0]] = distance[sorted_front[-1]] = float('inf')
        for i in range(1, len(sorted_front) - 1):
            distance[sorted_front[i]] += (
                objectives[sorted_front[i + 1]][m] - objectives[sorted_front[i - 1]][m]
            ) / (max(o[m] for o in objectives) - min(o[m] for o in objectives) + 1e-6)

    return distance