# copied from https://github.com/tsartsaris/TSPLIB-python-parser/blob/master/parser.py

import re

cities_set = []
cities_tups = []
cities_dict = {}

def read_tsp_data(tsp_name):
    with open(tsp_name) as f:
        content = f.read().splitlines()
        cleaned = [x.lstrip() for x in content if x != ""]
        return cleaned

def detect_dimension(in_list):
    non_numeric = re.compile(r'[^\d]+')
    for element in in_list:
        if element.startswith("DIMENSION"):
            return non_numeric.sub("",element)

def get_edge_type(data):
    non_numeric = re.compile(r'[^\d]+')
    for element in data:
        if element.startswith("EDGE_WEIGHT_TYPE"):
            edge_type = element.split(':', 1)[1].strip()
            return edge_type

def get_cities(list,dimension):
    dimension = int(dimension)
    for item in list:
        for num in range(1, dimension + 1):
            if item.startswith(str(num)):
                index, space, rest = item.partition(' ')
                if rest not in cities_set:
                    cities_set.append(rest)
    return cities_set

def city_tup(list):
    for item in list:
        first_coord, space, second_coord = item.partition(' ')
        cities_tups.append((first_coord.strip(), second_coord.strip()))
    return cities_tups

def create_cities_dict(cities_tups):
    return dict(zip((range(1,len(cities_tups)+1)),cities_tups))
