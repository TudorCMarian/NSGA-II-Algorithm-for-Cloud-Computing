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


# def crowding_distance_assignment(front, objectives):
#     distance = [0] * len(front)
#     num_objectives = len(objectives[0])

#     for m in range(num_objectives):
#         sorted_front = sorted(front, key=lambda sol: sol[m])  # Sortăm soluțiile direct după obiectivul m
#         if len(sorted_front) == 0:
#             return [0] * len(front)
#         elif len(sorted_front) == 1:
#             distance[0] = float('inf')  # Singura soluție primește infinit

#         # Calculăm distanța de aglomerare
#         for i in range(1, len(sorted_front) - 1):
#             distance[i] += (
#                 (sorted_front[i + 1][m] - sorted_front[i - 1][m])
#                 / (max(o[m] for o in objectives) - min(o[m] for o in objectives) + 1e-6)
#             )

#     return distance

# def crowding_distance_assignment(front, objectives):
#     """Calculate crowding distance for a front of solutions.
#     Args:
#         front (list): Indices of solutions in the current front.
#         objectives (list): List of objective values for all solutions [[obj1, obj2], ...].
#     Returns:
#         list: Crowding distances for the front.
#     """
#     # Initializare distanțe
#     distance = [0] * len(front)

#     # Separăm obiectivele în coloane
#     values1 = [objectives[i][0] for i in front]
#     values2 = [objectives[i][1] for i in front]

#     # Sortăm soluțiile după primul obiectiv
#     sorted1 = sorted(range(len(front)), key=lambda i: values1[i])
#     sorted2 = sorted(range(len(front)), key=lambda i: values2[i])

#     # Setăm distanțele extreme la infinit
#     distance[sorted1[0]] = float('inf')
#     distance[sorted1[-1]] = float('inf')
#     distance[sorted2[0]] = float('inf')
#     distance[sorted2[-1]] = float('inf')

#     # Calculăm distanțele pentru soluțiile interioare
#     for k in range(1, len(front) - 1):
#         if max(values1) - min(values1) != 0:  # Protecție împotriva împărțirii la 0
#             distance[sorted1[k]] += (
#                 values1[sorted1[k + 1]] - values1[sorted1[k - 1]]
#             ) / (max(values1) - min(values1))

#         if max(values2) - min(values2) != 0:
#             distance[sorted2[k]] += (
#                 values2[sorted2[k + 1]] - values2[sorted2[k - 1]]
#             ) / (max(values2) - min(values2))

#     return distance
