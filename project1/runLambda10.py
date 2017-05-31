#!/usr/local/opt/python3/bin/python3.6

from manualScript import *

def main():
    algorithms = (make_oneLambdaEA(10),)
    problems = (one_max, leading_ones)
    evaluate_all(np.arange(25, 201, 25), algorithms, problems, only_greater=True, filename_suffix=" - l10")

if __name__ == "__main__":
    main()
