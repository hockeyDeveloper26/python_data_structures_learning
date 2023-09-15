# From https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12371822#questions

#   1 ------- 2 --------0
#    \       /
#     \     /
#      \   /
#        3

# Edge List
graph_edg = [[0,2], [2,3], [2,1], [1,3]]

# Think of this as mapping out nodes
# [0,2] creates Node 0 and Node 2 with a connection between them
# [2,3] connects Node 2 to created Node 3 with a connection between them
# [2,1] connects Node 2 to created Node 1 with a connection between them
# [1,3] connects Node 1 to Node 3 with a connection between them

# Adjacent List
graph_adj = [[2], [2,3], [0,1,3], [1,2]]

# Represent [Node 0[conncetions], Node 1[conncetions], Node 2[conncetions], Node 3[conncetions]]


# Adjacent Matrix
graph_adj_mat = [
    [0, 0, 1, 0],   # Represents Node 0 and the Nodes its connected to
    [0, 0, 1, 1],   # Represents Node 1 and the Nodes its connected to
    [1, 1, 0, 1],   # Represents Node 2 and the Nodes its connected to
    [0, 1, 1, 0]    # Represents Node 3 and the Nodes its connected to
]