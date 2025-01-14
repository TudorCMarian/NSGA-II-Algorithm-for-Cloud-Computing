##########################################################################
#                                                                        #
#  Copyright:   (c) 2024, Paul Aflorei                                   #
#  E-mail:      paul-bogdan.aflorei@student.tuiasi.ro                    #
#  Name:        fast_nondominated_sort.py                                #
#                                                                        #
#  This code and information are provided "as is" without warranty of    #
#  any kind, either expressed or implied, including but not limited      #
#  to the implied warranties of merchantability or fitness for a         #
#  particular purpose. You are free to use this source code in your      #
#  applications as long as the original copyright notice is included.    #
#                                                                        #
##########################################################################

def fast_nondominated_sort(objectives):
    print(f"Objectives: {objectives}")
    S = [[] for _ in range(len(objectives))]
    front = [[]]
    n = [0] * len(objectives)
    rank = [0] * len(objectives)

    for p in range(len(objectives)):
        for q in range(len(objectives)):
            if dominates(objectives[p], objectives[q]):
                S[p].append(q)
            elif dominates(objectives[q], objectives[p]):
                n[p] += 1
        if n[p] == 0:
            rank[p] = 0
            front[0].append(p)
        print(f"Solution {p}: S={S[p]}, n={n[p]}, rank={rank[p]}")

    i = 0
    while front[i]:
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i + 1
                    Q.append(q)
        print(f"Front {i}: {front[i]}")

        i += 1
        front.append(Q)

    del front[-1]  # Remove the last empty front
    print(f"Final fronts: {front}")
    return front

def dominates(p, q):
    print(f"Comparing {p} and {q}")
    result = all(x <= y for x, y in zip(p, q)) and any(x < y for x, y in zip(p, q))
    print(f"Result: {result}")
    return result