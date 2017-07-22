import pandas as pd
import numpy as np
import csv

def process_semesters(students, target_func):
    result = pd.DataFrame(columns=['hash', 'Team', 'Semester', 'Sex', 'Discipline', 'Nationality'])
    for semester in ('WT-15', 'ST-16', 'WT-16', 'ST-17'):
        sem_students = students[students['Semester'] == semester]
        assert len(sem_students) in (80, 81),\
            'Expected 80 or 81 students but got {}'.format(len(students))
        partial_result = target_func(sem_students, semester)
        result = pd.concat([result, partial_result], ignore_index=True)
    return result

def store_teaming(teaming, filename=None):
    # Use the same format as used for the input data
    return teaming.to_csv(filename, quoting=csv.QUOTE_ALL, index=False,
                          columns=['hash', 'Team', 'Semester'])

def print_metric(metric_output, teaming_name):
    print('Multi-objective metric for {}: '.format(teaming_name) +
          'GenderBalance={:.2f}, Disciplines={:.2f}'.format(*metric_output[:2]) +
          ', Nationalities={:.2f}, Collision={:.2f}'.format(*metric_output[2:]))

#------------------------------------------------------------------------------#
# Teaming algorithms
#------------------------------------------------------------------------------#

def arbitrary_teaming(students, semester):
    groups = []
    for i in range(15):
        team = students[i*5:(i+1)*5]
        groups.extend((x['hash'], i+1, x['Semester'], x['Sex'], x['Discipline'], x['Nationality'])
                      for _, x in team.iterrows())
    groups.extend((x['hash'], 16, x['Semester'], x['Sex'], x['Discipline'], x['Nationality'])
                  for _, x  in students[75:].iterrows())
    grouped = pd.DataFrame(groups, columns=['hash', 'Team', 'Semester', 'Sex', 'Discipline', 'Nationality'])
    return grouped

def intra_diversity_teaming(students, semester):
    pass
