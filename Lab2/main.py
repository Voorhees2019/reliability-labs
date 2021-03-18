from functools import reduce
from copy import deepcopy


def get_uptime_probability(p_lst=None, matrix=None):
    global p_list

    def get_all_routes(vertex, previous_vertex):
        try:
            if previous_vertex != n:
                if matrix_connections[vertex][previous_vertex:].count(1) > 0:
                    idx = matrix_connections[vertex].index(1, previous_vertex)
                    route.append(idx)
                    get_all_routes(idx, 0)
                else:
                    if matrix_connections[vertex].count(0) == n:
                        routes.append(route[:])
                    route.remove(vertex)
                    if route:
                        get_all_routes(route[-1], vertex + 1)
            else:
                route.remove(vertex)
                if route:
                    get_all_routes(route[-1], vertex + 1)
        except RecursionError as e:
            print(f'[ERROR] {type(e).__name__}. Incorrect input matrix. Is there a loop? ')
            exit(1)

    # retrieving the data

    try:
        with open('data.txt', 'r') as file:
            matrix_connections = []
            while line := file.readline():
                line = line.strip()
                if not line: continue
                elif ',' in line: p_list = [float(i) for i in line.split(', ')]
                elif line.startswith('0 ') or line.startswith('1 '):
                    matrix_connections.append([int(num) for num in line.split(' ')])
    except:
        print('[ERROR] Incorrect input data. Check \'data.txt\' file.')
        exit(1)
    else:
        if p_lst:
            p_list = p_lst
        if matrix:
            matrix_connections = matrix

    try:
        transposed_matrix = [[matrix_connections[j][i] for j in range(len(matrix_connections))] for i in range(len(matrix_connections[0]))]
    except:
        print('[ERROR] Incorrect input matrix.')
        exit(1)
    start_vertexes = []
    end_vertexes = []
    routes = []
    route = []
    working_routes = []
    P = 0
    try:
        n = len(p_list)
    except:
        print('[ERROR] Incorrect input p_list.')
        exit(1)

    # checking input data

    if n < 1:
        print("[ERROR] Empty possibilities list")
        exit(1)

    for i in p_list:
        try:
            if i > 1 or i <= 0:
                raise
        except:
            print("[ERROR] Incorrect possibilities list. Possibility must be in range (0, 1]")
            exit(1)

    if len(matrix_connections) != n:
        print("[ERROR] Incompatible matrix of connections")
        exit(1)
    else:
        for i in matrix_connections:
            if i.count(0) + i.count(1) != n:
                print("[ERROR] Incompatible matrix of connections")
                exit(1)

    for i in range(len(matrix_connections)):
        if transposed_matrix[i].count(0) == n:
            start_vertexes.append(i)
        if matrix_connections[i].count(0) == n:
            end_vertexes.append(i)

    if not start_vertexes:
        print("[ERROR] No start vertexes was found")
        exit(1)
    elif not end_vertexes:
        print("[ERROR] No end vertexes was found")
        exit(1)

    # main calculation
    if n == 1:
        print(f"[SUCCESS] System uptime probability = {p_list[0]}")
        exit(0)

    for i in start_vertexes:
        route.append(i)
        get_all_routes(i, 0)

    if not routes:
        print("[ERROR] No routes was found")
        exit(1)

    for route in routes:
        working_conditions = [[]]
        for i in range(n):
            if i in route:
                for j in range(len(working_conditions)):
                    working_conditions[j].append(1)
            else:
                working_conditions.extend(deepcopy(working_conditions))
                for k in range(int(len(working_conditions) / 2)):
                    working_conditions[k].append(0)
                    working_conditions[-k - 1].append(1)
        for z in working_conditions:
            if z not in working_routes:
                working_routes.append(z)

    for working_route in working_routes:
        tmp_lst = list(map(lambda x, y: y if x == 1 else 1-y, working_route, p_list))
        P += reduce(lambda x, y: x*y, tmp_lst)

    return P


if __name__ == '__main__':
    P = get_uptime_probability()
    print(f"[SUCCESS] System uptime probability = {P}")
