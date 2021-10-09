
class Household:
    def __init__(self, name, labour, propensity_to_save, initial_accounts):
        """
        This method initialises an agent and its properties.

        Agents have several properties, that can either be state variables (if they change),
        or static parameters. There is a distinction between agent specific parameters
        and parameters that are the same for all agents and could thus be seen
        as global parameters.

        The following inputs are used to initialise the agent
        :param name: unique agent identifier , integer
        :param type: household, firm, bank, central_bank, or service_provider, string
        :param assets: asset types, dictionary
        :param liabilities: liability types, dictionary
        """
        # state variables
        # agent specific parameters
        self.name = name
        self.labour = labour
        self.propensity_to_save = propensity_to_save
        self.accounts = initial_accounts

    def __repr__(self):
        """
        :return: String representation of the trader
        """
        return 'Household' + str(self.name)
