import numpy as np
import networkx as nx
import random
import copy
import os
import pandas as pd

from cbdcsim.agent import Agent

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
        self.agents = [Agent(x) for x in range(parameters["number_of_agents"])]
        graph = nx.Graph()

        # 3 Next, we create the a city wide network structure of recurring contacts by linking all agents of types
        for agent in self.agents:
            pass
            # link households to banks

            # link firms to banks

            # link banks to CB

            # link service provider to ....?

            # for ca in location_closest_agents:
            #     city_graph.add_edge(agent.name, ca.name, label='other')

        self.network = graph

        # rename agents to reflect their new position
        for idx, agent in enumerate(self.agents):
            agent.name = idx

        # add agent to the network structure
        for idx, agent in enumerate(self.agents):
            pass
            #self.network.nodes[idx]['agent'] = agent
