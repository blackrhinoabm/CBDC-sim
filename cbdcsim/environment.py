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

    def __init__(self, parameters, bank_parameters, household_parameters, firm_parameters, cb_parameters):
        """
        This method initialises the environment and its properties.

        :param seed: used to initialise the random generators to ensure reproducibility, int
        :param parameters: contains all model parameters, dictionary
        """
        self.parameters = parameters
        self.measurement = {'period': [], 'to_agent': [], 'from_agent':[], 'settlement_type': [], 'amount': [], 'description': []}

        # TODO debug
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
                Household('f{}'.format(idx), household_pars["labour"], household_pars['propensity_to_save'],
                          {'deposits': household_pars['initial_deposits']}))

        self.central_bank = [CentralBank('cb1')]

        self.transactions_list = {'period': [], 'to_agent': [], 'from_agent_': [], 'settlement_type': [], 'amount': []}
        graph = nx.Graph()

        # 3 Next, we create the network structure linking Banks, Households, and Firms
        for bank in self.banks:
            pass
            # link households to banks

            # link firms to banks

            # link banks to CB

            # link service provider to ....?

            # for ca in location_closest_agents:
            #     city_graph.add_edge(agent.name, ca.name, label='other')

        self.network = graph

        # rename agents to reflect their new position
        for idx, agent in enumerate(self.banks):
            agent.name = idx

        # add agent to the network structure
        for idx, agent in enumerate(self.banks):
            pass
            #self.network.nodes[idx]['agent'] = agent


