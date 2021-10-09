import networkx as nx
import pandas as pd

from cbdcsim.bank import Bank
from cbdcsim.firm import Firm
from cbdcsim.household import Household


class Environment:
    """
    The environment class contains the agents in a network structure
    """

    def __init__(self, parameters):
        """
        This method initialises the environment and its properties.

        :param seed: used to initialise the random generators to ensure reproducibility, int
        :param parameters: contains all model parameters, dictionary
        """
        self.parameters = parameters
        self.measurement = {'period': [], 'to_agent': [], 'from_agent':[], 'settlement_type': [], 'amount': [], 'description': []}
        self.banks = [Bank(x, parameters["interest_deposits"], parameters["interest_loans"],
                           {'deposits': -parameters['initial_deposits'] / parameters["num_banks"]}) for x in range(
            parameters["num_banks"])]
        self.households = [Household(x, parameters["labour"], parameters["propensity_to_save"],
                                     {'deposits': parameters['initial_deposits'] / (parameters["num_households"] + parameters["num_firms"])}) for x in range(
            parameters["num_households"])]
        self.firms = [Firm(x, parameters["productivity"],
                           {'deposits': parameters['initial_deposits'] / (parameters["num_households"] + parameters["num_firms"])}) for x in range(parameters["num_firms"])]
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


