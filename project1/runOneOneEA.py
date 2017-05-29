#!/usr/local/opt/python3/bin/python3.6

from manualScript import *

def main():
    algorithms = (oneOneEA,)
    problems = (one_max, leading_ones, jump, royal_roads, bin_val)
    evaluate_all(np.arange(25, 201, 25), algorithms, problems, only_greater=False)

if __name__ == "__main__":
    main()