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

# Step 4: Fast Nondominated Sort
def fast_nondominated_sort(objectives):
    """Perform fast nondominated sorting.
    Args:
        objectives (list): List of (cost, time) tuples.
    Returns:
        list: A list of fronts, where each front is a list of indices.
    """
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

    i = 0
    while front[i]:
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i + 1
                    Q.append(q)
        i += 1
        front.append(Q)

    del front[-1]  # Remove the last empty front
    return front

def dominates(p, q):
    """Check if solution p dominates solution q.
    Args:
        p (tuple): Objectives of solution p.
        q (tuple): Objectives of solution q.
    Returns:
        bool: True if p dominates q, False otherwise.
    """
    return all(x <= y for x, y in zip(p, q)) and any(x < y for x, y in zip(p, q))