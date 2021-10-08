import random
import numpy as np
import pandas as pd


def updater(environment, data_folder='output_data/', seed=0):
    """
    This function is used to run / simulate the model.

    :param environment: contains the parameters and agents, Environment object
    :param seed: used to initialise the random generators to ensure reproducibility, int
    :param data_folder:  string of the folder where data output files should be created
    :return: environment object containing the updated agents, Environment object
    """
    # 1 set monte carlo seed
    np.random.seed(seed)
    random.seed(seed)

    # initialisation:
    labour_growth = environment.parameters['labour_growth']  # the labor-force L proportional growth rate (n)
    efficiency_growth = environment.parameters[
        'efficiency_growth']  # the labor-efficiency E proportional growth rate (g)
    savings_rate = environment.parameters['savings_rate']  # the share of production Y that is saved and invested (s)
    depreciation_rate = environment.parameters['depreciation_rate']  # the capital depreciation rate (δ)
    production_elasticity = environment.parameters[
        'production_elasticity']  # the elasticitiy of production Y with respect to capital θ
    labour_0 = environment.parameters['labour_zero']  # labour force T=0 (L_0)
    efficiency_0 = environment.parameters['efficiency_zero']  # labour efficiency T=0 (E_0)
    capital_0 = environment.parameters['capital_zero']  # capital at T=0 (κ_0)
    time = environment.parameters['time']  # simulation time

    environment.data = pd.DataFrame()
    labour = [labour_0]
    labour_efficiency = [efficiency_0]
    capital_intensity = [capital_0]
    production = []
    capital = []
    output_per_worker = []

    # determine labour force size, labour efficiency, and capital intensity over time
    for t in range(time):
        labour = labour + [labour[t] * np.exp(labour_growth)]
        labour_efficiency = labour_efficiency + [labour_efficiency[t] * np.exp(efficiency_growth)]
        capital_intensity = capital_intensity + [capital_intensity[t] * (1 + (
                savings_rate / capital_intensity[t] - (labour_growth + efficiency_growth + depreciation_rate)) / (
                                                                                 1 + production_elasticity))]

    # determine production, capital, and output per worker
    for t in range(time + 1):
        production = production + [(capital_intensity[t] ** production_elasticity) * labour[t] * labour_efficiency[t]]
        capital = capital + [(capital_intensity[t] * production[t])]
        output_per_worker = output_per_worker + [production[t] / labour[t]]

    # fill dataframe in df
    environment.data['labour'] = labour
    environment.data['labour_efficiency'] = labour_efficiency
    environment.data['capital_intensity'] = capital_intensity
    environment.data['production'] = production
    environment.data['capital'] = capital
    environment.data['output_per_worker'] = output_per_worker

    return environment
