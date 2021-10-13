import networkx as nx
import pandas as pd

from cbdcsim.bank import Bank
from cbdcsim.firm import Firm
from cbdcsim.household import Household
from cbdcsim.central_bank import CentralBank


class Environment:
    """
    The environment class contains the agents in a network structure
    """

    def __init__(self, parameters, bank_parameters, household_parameters, firm_parameters, cb_parameters, graph):
        """
        This method initialises the environment and its properties.

        :param seed: used to initialise the random generators to ensure reproducibility, int
        :param parameters: contains all model parameters, dictionary
        """
        self.parameters = parameters
        self.measurement = {'period': [], 'to_agent': [], 'from_agent':[], 'settlement_type': [], 'amount': [], 'description': []}

        self.banks = []
        for idx, bank_pars in enumerate(bank_parameters):
            self.banks.append(Bank('b{}'.format(idx), bank_pars["interest_deposits"], bank_pars["interest_loans"],
                                   {'deposits': -bank_pars['initial_deposits']}))

        self.firms = []
        for idx, firm_pars in enumerate(firm_parameters):
            self.firms.append(Firm('f{}'.format(idx), firm_pars["productivity"], {'deposits': firm_pars['initial_deposits']}))

        self.households = []
        for idx, household_pars in enumerate(household_parameters):
            self.households.append(
                Household('hh{}'.format(idx), household_pars["labour"], household_pars['propensity_to_save'],
                          {'deposits': household_pars['initial_deposits']}))

        self.central_bank = [CentralBank('cb1')]

        self.transactions_list = {'period': [], 'to_agent': [], 'from_agent_': [], 'settlement_type': [], 'amount': []}
        self.network = graph


