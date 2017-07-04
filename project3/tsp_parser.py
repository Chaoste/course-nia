import numpy as np
import itertools as it
from haversine import haversine

"""
a.) EDGE_WEIGHT_FORMAT: FULL_MATRIX
DISPLAY_DATA_TYPE: TWOD_DISPLAY
EDGE_WEIGHT_SECTION
b.) EDGE_WEIGHT_FORMAT: LOWER_DIAG_ROW
EDGE_WEIGHT_SECTION
c.) EDGE_WEIGHT_FORMAT: FUNCTION
DISPLAY_DATA_TYPE: COORD_DISPLAY
NODE_COORD_SECTION
d.) EDGE_WEIGHT_TYPE : ATT
NODE_COORD_SECTION
e.) EDGE_WEIGHT_TYPE: EUC_2D
NODE_COORD_SECTION
f.) EDGE_WEIGHT_TYPE : EUC_2D
NODE_COORD_SECTION
"""

# Numpy won't be very efficient but it also allows very large integers (far above 64 bits)
BIG_INT = 'object'

# Old function for generating an adjacent matrix based on coordinates
def deprecated_process_graph(G):
    n = len(G['coords'])
    # Assuming that the ids are from 1 to n
    N = np.arange(n)
    positions = np.zeros((n, 2), dtype=np.float)
    # Collect all positions assuming that the nodes are sorted by id
    positions = [(float(x), float(y)) for x, y in G['coords'].values()]
    # Generate adjacent matrix
    am = np.zeros((n, n), dtype=np.float)
    if (G['edge_type'] == "GEO"):
        for i, j in it.combinations(N, 2):
            am[i, j] = am[j, i] = haversine(positions[i], positions[j])
    ## Generate adjacent matrix containing the euclidean distances between nodes
    #am = np.zeros((n, n), dtype=np.float)
    #for i, j in it.combinations(N, 2):
    #    i_x, i_y = positions[i]
    #    j_x, j_y = positions[j]
    #    am[i, j] = am[j, i] = np.hypot((i_x - j_x), (i_y - j_y))
    return N, n, am
def deprecated_load_data():
    data = read_tsp_data("data/burma14.tsp")
    print(data)
    graph['edge_type'] = get_edge_type(data)
    if (graph['edge_type'] != "GEO"):
        raise Exception("edge_type not implemented", graph['edge_type'])
    dimension = detect_dimension(data)
    cities_set = get_cities(data,dimension)
    cities_tups = city_tup(cities_set)
    cities_dict = create_cities_dict(cities_tups)
    graph['coords'] = cities_dict
    return graph
    return dict([(1, ('38.24', '20.42')), (2, ('39.57', '26.15')), (3, ('40.56', '25.32')), (4, ('36.26', '23.12')), (5, ('33.48', '10.54')), (6, ('37.56', '12.19')), (7, ('38.42', '13.11')), (8, ('37.52', '20.44')), (9, ('41.23', '9.10')), (10, ('41.17', '13.05')), (11, ('36.08', '-5.21')), (12, ('38.47', '15.13')), (13, ('38.15', '15.35')), (14, ('37.51', '15.17')), (15, ('35.49', '14.32')), (16, ('39.36', '19.56'))])

def get_file_info(tsp_name):
    # Transform file content into a object containing all information
    problem = []
    tsp_name = '{}.tsp'.format(tsp_name) if not tsp_name.endswith('.tsp') else tsp_name
    with open(tsp_name) as f:
        # Load all lines at once
        lines = f.read().splitlines()
        # Remove empty lines
        lines = [x for x in lines if x != '']
    i = 0
    while ':' in lines[i]:
        key, value = [x.strip() for x in lines[i].split(':')]
        key = key.lower()
        if key == 'dimension':
            value = int(value)
        problem.append((key, value))
        i += 1
    problem.append(('definition_type', lines[i].strip()))
    i += 1
    definitions = ''
    while 'EOF' not in lines[i] and lines[i].lstrip()[0].isdigit():
        definitions += lines[i] + ' '
        i += 1
    problem.append(('definition', definitions))
    return dict(problem)

def parse_half_edge_weights(problem):
    # Examples: gr17, gr21, gr24, gr48
    numbers = [int(x) for x in problem['definition'].split()]
    cities = int(problem['dimension'])
    am = np.zeros((cities, cities), dtype=BIG_INT)
    col = 0
    row = 0
    for i, value in enumerate(numbers):
        am[row, col] = am[col, row] = numbers[i]
        if row < col:
            row += 1
        else:
            row = 0
            col += 1
    return am

def parse_full_edge_weights(problem):
    # Examples: bays29
    numbers = [int(x) for x in problem['definition'].split()]
    cities = int(problem['dimension'])
    am = np.array(numbers, dtype=BIG_INT).reshape((cities, cities))
    return am

def parse_node_coord_section(problem, dtype=float):
    # Examples: att48, berlin52, burma14, fnl4461, gr96
    numbers = [dtype(x) for x in problem['definition'].split()]
    cities = int(problem['dimension'])
    # Ignore ID
    coords =  np.array(numbers, dtype=dtype).reshape(cities, 3)[:, 1:]
    # Generate adjacent matrix containing the euclidean distances between nodes
    am = np.zeros((cities, cities), dtype=dtype)
    for i, j in it.combinations(range(cities), 2):
        # TODO: Do we need the haversine package for calculating the distance
        # (assuming the coords are latitude and longitude)
        # am[i, j] = am[j, i] = haversine(positions[i], positions[j])
        i_x, i_y = coords[i]
        j_x, j_y = coords[j]
        am[i, j] = am[j, i] = np.hypot((i_x - j_x), (i_y - j_y))
    return am

def parse_distances(problem):
    if problem['definition_type'] == 'EDGE_WEIGHT_SECTION':
        # We get a full or half adjacent matrix containing the distances
        if 'edge_weight_format' in problem and problem['edge_weight_format'] == 'LOWER_DIAG_ROW':
            # Only half of the distance matrix given as integer
            return parse_half_edge_weights(problem)
        elif 'edge_weight_format' in problem and problem['edge_weight_format'] == 'FULL_MATRIX':
            # Full adjacent matrix
            return parse_full_edge_weights(problem)
        else:
            raise ValueError('Unsupported tsp data format')
    elif problem['definition_type'].upper() == 'NODE_COORD_SECTION':
        if 'display_data_type' in problem and problem['display_data_type'] == 'COORD_DISPLAY':
            # Float numbers
            return parse_node_coord_section(problem, float)
        else:
            # Integer numbers (64 bit due to later occuring overflows
            # e.g. when taking to the power of 4)
            return parse_node_coord_section(problem, BIG_INT)
    else:
        raise ValueError('Unsupported tsp data format')

def get_optimal_solution(problem, opt_file):
    problem_name = problem['name'].lower()
    with open(opt_file) as f:
        for line in f:
            line = line.lower()
            if line.startswith(problem_name):
                _, opt_value = line.split(':')
                opt_value = opt_value.strip()
                # For some reason there might be multiple solutions
                if opt_value[0] == '[':
                    # TODO: Parse array and take the minimum
                    break
                else:
                    return int(opt_value)
    print('WARNING! Couldn\'t find optimal solution')
    return -1

def load_problem(tsp_name, opt_file='data/opt_solutions.txt'):
    problem = get_file_info(tsp_name)
    problem['distances'] = parse_distances(problem)
    problem['opt'] = get_optimal_solution(problem, opt_file)
    del problem['definition']
    return problem

if __name__ == '__main__':
    problem = load_problem('data/burma14')  # bays29, gr17, burma14
    print(problem)
