import pandas as pd
import numpy as np
import csv

def process_semesters(students, target_func):
    result = pd.DataFrame(columns=['hash', 'team', 'Semester'])
    for semester in ('WT-15', 'ST-16', 'WT-16', 'ST-17'):
        sem_students = students[students['Semester'] == semester]
        assert len(sem_students) in (80, 81),\
            'Expected 80 or 81 students but got {}'.format(len(students))
        partial_result = target_func(sem_students, semester)
        result = pd.concat([result, partial_result], ignore_index=True)
    return result

def store_teaming(teaming, filename=None):
    # Use the same format as used for the input data
    return teaming.to_csv(filename, quoting=csv.QUOTE_ALL, index=False)

#------------------------------------------------------------------------------#
# Teaming algorithms
#------------------------------------------------------------------------------#

def arbitrary_teaming(students, semester):
    groups = []
    for i in range(15):
        team = students[i*5:(i+1)*5]
        groups.extend((hash_, i+1, semester) for hash_ in team['hash'])
    groups.extend((hash_, 16, semester) for hash_ in students[75:]['hash'])
    grouped = pd.DataFrame(groups, columns=['hash', 'team', 'Semester'])
    return grouped

def intra_diversity_teaming(students, semester):
    pass
