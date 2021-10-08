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
    seed = kwargs.get('seed')
    output_folder_path = kwargs.get('output_folder_path')
    input_folder_path = kwargs.get('input_folder_path')

    # formulate paths to initialisation folder and seed within input folder
    if kwargs.get('initial_seeds_folder'):
        inititialisation_path = kwargs.get('initial_seeds_folder')
        click.echo('Modified initialisations path: {}'.format(inititialisation_path))
    else:
        inititialisation_path = os.path.join(input_folder_path, 'initialisations')

    seed_path = os.path.join(inititialisation_path, 'seed_{}.pkl'.format(seed))
    if not os.path.exists(seed_path):
        click.echo(seed_path + ' not found', err=True)
        click.echo('Error: specify a valid seed')
        return

    # open the seed pickle object as an environment
    data = open(seed_path, "rb")
    list_of_objects = pickle.load(data)
    environment = list_of_objects[0]

    # add contacts section to csv light DataFrame TODO remove after re-initialisation
    environment.infection_quantities['contacts'] = []

    # initialise logging
    logging.basicConfig(filename=os.path.join(output_folder_path,
                                              'simulation_seed{}.log'.format(seed)), filemode='w', level=logging.DEBUG)
    logging.info('Start of simulation seed{} with arguments -i ={}, -o={}'.format(seed,
                                                                                  input_folder_path,
                                                                                  output_folder_path))

    # update optional parameters
    if kwargs.get('sensitivity_config_file_path'):
        config_path = kwargs.get('sensitivity_config_file_path')
        if not os.path.exists(config_path):
            click.echo(config_path + ' not found', err=True)
            click.echo('Error: specify a valid path to the sensitivity config file')
            return
        else:
            with open(config_path) as json_file:
                config_file = json.load(json_file)

                for param in config_file:
                    environment.parameters[param] = config_file[param]

    labour_growth = kwargs.get('labour_growth')  # the labor-force L proportional growth rate (n)
    print('labour_growth = ', labour_growth)
    efficiency_growth = kwargs.get('efficiency_growth')  # the labor-efficiency E proportional growth rate (g)
    print('efficiency_growth = ', efficiency_growth)
    savings_rate = kwargs.get('savings_rate')  # the share of production Y that is saved and invested (s)
    print('savings_rate = ', savings_rate)
    depreciation_rate = kwargs.get('depreciation_rate')  # the capital depreciation rate (δ)
    print('depreciation_rate = ', depreciation_rate)
    production_elasticity = kwargs.get(
        'production_elasticity')  # the elasticitiy of production Y with respect to capital θ
    print('production_elasticity = ', production_elasticity)
    labour_0 = kwargs.get('labour_zero')  # labour force T=0 (L_0)
    print('labour_zero = ', labour_0)
    efficiency_0 = kwargs.get('efficiency_zero')  # labour efficiency T=0 (E_0)
    print('efficiency_zero = ', efficiency_0)
    capital_0 = kwargs.get('capital_zero')  # capital at T=0 (κ_0)
    print('capital_zero = ', capital_0)
    time = kwargs.get('time')  # simulation time
    print('time = ', time)

    output_folder_path = kwargs.get('output_folder_path')

    # Simulate the model
    environment = updater(environment=environment,
                          data_folder=output_folder_path,
                          data_output=environment.parameters["data_output"])

    return environment
