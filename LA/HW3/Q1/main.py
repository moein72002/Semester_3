import numpy as np

n = int(input())
adjacency_matrix = []
for i in range(n):
    adjacency_matrix.append(list(map(int, input().split())))

A = np.array(adjacency_matrix)
B = A
C = A
vertex_number = -1
graph_radius = 0

k = 0
done = 0
while done == 0:
    graph_radius += 1
    if graph_radius == n:
        graph_radius = -1
        vertex_number = -1
        break

    for i in range(n):
        counter = 0
        for j in range(n):
            if i != j and C[i][j] > 0:
                counter += 1
            elif i != j and C[i][j] == 0:
                break
        if counter == n - 1:
            vertex_number = i
            done = 1
            break
    B = np.matmul(A, B)
    C = np.add(C, B)

print(vertex_number)
print(graph_radius)
