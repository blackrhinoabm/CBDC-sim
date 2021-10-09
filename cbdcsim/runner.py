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

    time = kwargs.get('time')  # simulation time
    environment.parameters['time'] = time
    print('time = ', time)

    # Simulate the model
    environment = updater(environment=environment,
                          data_folder=output_folder_path)

    return environment
