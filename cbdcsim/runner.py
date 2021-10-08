import click
import os
import pickle
import json
import logging
import numpy as np
import random
import pandas as pd
import scipy.stats as stats

from cbdcsim.updater import updater


def runner(environment, **kwargs):
    """
    This function is used to update parameters

    :param kwargs:
    :return:
    """

    # store often used arguments in temporary variable
    output_folder_path = kwargs.get('output_folder_path')
    #input_folder_path = kwargs.get('input_folder_path')

    labour_growth = environment.parameters['labour_growth']  # the labor-force L proportional growth rate (n)
    print('labour_growth = ', labour_growth)
    efficiency_growth = environment.parameters['efficiency_growth']  # the labor-efficiency E proportional growth rate (g)
    print('efficiency_growth = ', efficiency_growth)
    savings_rate = environment.parameters['savings_rate']  # the share of production Y that is saved and invested (s)
    print('savings_rate = ', savings_rate)
    depreciation_rate = environment.parameters['depreciation_rate']  # the capital depreciation rate (δ)
    print('depreciation_rate = ', depreciation_rate)
    production_elasticity = environment.parameters[
        'production_elasticity']  # the elasticitiy of production Y with respect to capital θ
    print('production_elasticity = ', production_elasticity)
    labour_0 = environment.parameters['labour_zero']  # labour force T=0 (L_0)
    print('labour_zero = ', labour_0)
    efficiency_0 = environment.parameters['efficiency_zero']  # labour efficiency T=0 (E_0)
    print('efficiency_zero = ', efficiency_0)
    capital_0 = environment.parameters['capital_zero']  # capital at T=0 (κ_0)
    print('capital_zero = ', capital_0)
    time = kwargs.get('time')  # simulation time
    environment.parameters['time'] = time
    print('time = ', time)

    # Simulate the model
    environment = updater(environment=environment,
                          data_folder=output_folder_path)

    return environment
