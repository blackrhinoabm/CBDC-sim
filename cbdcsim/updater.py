import random
import numpy as np
import pandas as pd
from cbdcsim.transaction import transact


def updater(environment, data_folder='output_data/', seed=0):
    """
    This function is used to run / simulate the model.

    :param environment: contains the parameters and agents, Environment object
    :param seed: used to initialise the random generators to ensure reproducibility, int
    :param data_folder:  string of the folder where data output files should be created
    :return: environment object containing the updated agents, Environment object
    """

    # time loop
    for t in range(environment.parameters['time']):
        # accruing interest on all deposits for banks
        for bank in environment.banks:
            for tranx in bank.accounts:
                if tranx == "deposits":
                    bank.accounts[tranx] = bank.accounts[tranx] + bank.accounts[tranx] * bank.interest_deposits

        # accruing interest on all deposits for firms
        for firm in environment.firms:
            for tranx in firm.accounts:
                if tranx == "deposits":
                    firm.accounts[tranx] = firm.accounts[tranx] + firm.accounts[tranx] * environment.parameters["interest_deposits"]
                    # record transaction
                    transact(environment, t, firm, environment.banks[0], tranx,
                             firm.accounts[tranx] * environment.parameters["interest_deposits"], 'interest deposits')

        # accruing interest on all deposits for households
        for household in environment.households:
            for tranx in household.accounts:
                if tranx == "deposits":
                    household.accounts[tranx] = household.accounts[tranx] + household.accounts[tranx] * environment.parameters["interest_deposits"]
                    # record transaction
                    transact(environment, t, household, environment.banks[1], tranx,
                             household.accounts[tranx] * environment.parameters["interest_deposits"], 'interest deposits')

    return environment
