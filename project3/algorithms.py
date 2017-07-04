import numpy as np
import itertools as it
import time
from matplotlib import pyplot as plt

'''
    Max-Mint Ant System for solving the traveling salesman problem
    Parameters:
        problem - parsed tsp containing adjacent matrix, optimal solution, etc.
    Optional values (given as keyword arguments):
        rho  (default: 1 / n)
        tau_min  (default: 1 / n**2)
        tau_max  (default: n - 1 / n)
        alpha  (default: 1)
        beta  (default: 0)
        wall_clock_time  (default: 600 [seconds])
'''
class MMAS:
    def __init__(self, problem, **kwargs):
        self.problem = problem
        self.n = self.problem['dimension']
        self.am = self.problem['distances']
        self.N = np.arange(self.n) # ids from 0 to n-1 (translate later if you want to print the route)
        self.start_time = None
        self.results = None
        self.wall_clock_time = kwargs.get('wall_clock_time') or 10 * 60
        # Pheromone values stored in an adjacent matrix (initial 1 / n for each edge, otherwise 0)
        self.tau = self._init_tau()
        # Parameters of the algorithm
        self.rho = kwargs.get('rho') or 1 / self.n
        self.tau_min = kwargs.get('tau_min') or 1 / self.n**2
        self.tau_max = kwargs.get('tau_max') or self.n - 1 / self.n
        self.alpha = kwargs.get('alpha') or 1
        self.beta = kwargs.get('beta') or 0

    def _init_tau(self):
        return np.array([[1 / self.n for x in range(self.n)] for y in range(self.n)], dtype=np.float)

    #--------------------------------------------------------------------------------------------------------------
    # Methods for execution
    #--------------------------------------------------------------------------------------------------------------

    def _route_length(self, x):
        # Sum up the distances between all traversed nodes
        return sum([self.am[x[i], x[i+1]] for i in range(len(x) - 1)]) + self.am[x[len(x) - 1], x[0]]

    def _is_optimum_found(self, x):
        # Optimal value found or the wall clock time is reached
        return (self._route_length(x) == self.problem['opt'] or
                time.time() - self.start_time > self.wall_clock_time)

    def _update_tau(self, route):
        # Update self.tau regarding the path x (list of visited nodes)
        # TODO rename
        tau = np.zeros((self.n, self.n), dtype=np.float)
        # Update all edges traversed by the given route
        for i in range(len(route) - 1):
            x, y = route[i], route[i + 1]
            tau[x, y] = tau[y, x] = min((1 - self.rho) * self.tau[x, y] + self.rho, self.tau_max)
        # Update all not traversed edges
        for x, y in it.combinations_with_replacement(self.N, 2):
            if not tau[x, y]:
                tau[x, y] = tau[y, x] = max((1 - self.rho) * self.tau[x, y], self.tau_min)
        self.tau = tau

    def _construct(self):
        # Create a route based on the pheromone values in self.tau
        route = np.empty(self.n, dtype=np.int)
        # Setup a visited array to prevent visiting a node twice
        visited = np.zeros(self.n, dtype=np.bool)
        # Start at a random node
        # TODO vllt nicht random?
        route[0] = np.random.randint(self.n)
        visited[route[0]] = True
        for i in range(self.n - 1):
            v_k = route[i]
            left_nodes = np.array([(z, self.tau[v_k, z]**self.alpha / self.am[v_k, z]**self.beta)
                                   for z in self.N if not visited[z]])
            # Some values might get below zero due to a overflow (see used dtype in tsp_parser)
            assert np.all(left_nodes >= 0), 'Values below zero! Used data types: {} and {} \nLeft nodes:\n{}'.format(
                self.tau.dtype, self.am.dtype, left_nodes)
            R = left_nodes[:, 1].sum()
            assert R != 0, 'route: {}, left: {}'.format(route, left_nodes)
            route[i + 1] = np.random.choice(left_nodes[:, 0], p=left_nodes[:, 1] / R)
            visited[route[i + 1]] = True
        return route

    def _averaged_results(self, N):
        # https://stackoverflow.com/questions/13728392/moving-average-or-running-mean
        rm = np.convolve(self.results, np.ones((N,))/N, mode='valid')
        filler = [None] * ((len(self.results) - len(rm)) // 2)
        return np.array(filler + list(rm) + filler)

    def plot(self):
        fig_length = max(8, min(18, len(self.results) // 400))
        fig, ax = plt.subplots(1, 1, figsize=(fig_length, 4))
        ax.plot(self.results)
        ax.plot(self._averaged_results(10), color="red")
        ax.plot(self._averaged_results(100), color="green")
        ax.set_xlim([0, len(self.results)])
        ax.set_title('MMAS - {}, best value: {:.2f} (OPT: {})'.format(
            self.problem['name'], self.best_x_value, self.problem['opt']))
        ax.set_xlabel('Epoch')
        ax.set_ylabel('Route length')
        fig.tight_layout()

    def __call__(self, plot=True):
        self.start_time = time.time()
        self.best_x = self._construct()
        self.best_x_value = self._route_length(self.best_x)
        self.results = [self.best_x_value]
        self._update_tau(self.best_x)
        while not self._is_optimum_found(self.best_x):
            x = self._construct()
            self.results.append(self._route_length(x))
            if self.results[-1] < self.best_x_value:
                self.best_x = x
                self.best_x_value = self.results[-1]
            self._update_tau(self.best_x)
        if plot:
            print('Stopped after {:.2f} minutes'.format((time.time() - self.start_time)/60))
            self.plot()
        return self.best_x_value, self.best_x
