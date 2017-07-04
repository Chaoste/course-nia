import numpy as np
import viz
import algorithms as algo
import itertools as it

def grid_search(problem, **kwargs):
    n = problem['dimension']
    alphas = kwargs.get('alphas') or [1]
    betas = kwargs.get('betas') or [0, 2, 4, 6]
    rhos = kwargs.get('rhos') or [1 / n]
    tau_mins = kwargs.get('tau_mins') or [1 / n**2]
    tau_maxs = kwargs.get('tau_maxs') or [n - 1 / n]
    wall_clock_time = kwargs.get('runtime') or 5
    shape = (len(alphas), len(betas), len(rhos), len(tau_mins), len(tau_maxs))
    costs = np.empty(shape, dtype=float)
    for ai, bi, ri, tmini, tmaxi in it.product(*[range(x) for x in shape]):
        alpha, beta, rho = alphas[ai], betas[bi], rhos[ri]
        tau_min, tau_max = tau_mins[tmini], tau_maxs[tmaxi]
        np.random.seed(0)
        mmas = algo.MMAS(problem, wall_clock_time=wall_clock_time, alpha=alpha,
                         beta=beta, rho=rho, tau_min=tau_min, tau_max=tau_max)
        route_length, _ = mmas(plot=False)
        costs[ai, bi, ri, tmini, tmaxi] = route_length
    # Collect example best parameters
    best_params = np.where(costs == costs.min())
    ai, bi, ri, tmini, tmaxi = next(zip(*best_params))
    opt_params = alphas[ai], betas[bi], rhos[ri], tau_mins[tmini], tau_maxs[tmaxi]
    return opt_params, costs

def plot_parameter_heatmap(costs, dim1, dim2):
    values1, label1 = dim1
    values2, label2 = dim2
    cost_map = costs.reshape(len(values1), len(values2))  # This works as long as the other dimensions are 1
    viz.heatmap(cost_map, 'Route length for {} vs. {}'.format(label1, label2), label2, label1, values2, values1, cbar=False)
    return
