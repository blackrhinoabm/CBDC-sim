import sys
import click
import os
import pandas as pd
import json
import logging
import networkx as nx

from cbdcsim.runner import runner
from cbdcsim.environment import Environment


@click.group()
@click.version_option("1.0.0")
def main():
    """
    An open source, easy-to-use-and-adapt, CBDC-simulation model.
    """
    pass


#
# @main.command()
# @click.option('--time', '-t', type=int, required=True, help="simulated periods")
# @click.option('--input_folder_path', '-i', type=click.Path(exists=True), required=True,
#               help="This should contain all necessary input files, specifically an initialisation folder")
# @click.option('--output_folder_path', '-o', type=click.Path(exists=True), required=True,
#               help="All simulation output will be deposited here")
def simple(**kwargs):
    """
    This function is used to run / simulate the simple model.
    It will output a csv file with data on simulated macroeconomic variables.

    :param kwargs: dictionary containing the following parameters
    labour_growth or -g: proportional labour growth, Float
    efficiency_growth or -eg: proportional efficiency growth, Float
    savings_rate or -s: percentage of income saved, Float
    depreciation_rate or -dr: how quickly capital depreciates, Float
    production_elasticity or -pe: path to output folder, Float
    labour_zero or -lz: savings rate, Float
    efficiency_zero or -ez: savings rate, Float
    time or -t: path that contain all necessary input files, Int
    capital_zero or -ce: path to output folder, Float
    output_folder_path or -lz: path to output folder, String

    :return: None
    """
    # 1 open parameters from json file
    input_folder_path = kwargs.get('input_folder_path')

    parameters_path = os.path.join(input_folder_path, 'parameters.json')
    if not os.path.exists(parameters_path):
        click.echo(parameters_path + ' not found', err=True)
        click.echo('No parameter file found')
        return

    with open(parameters_path) as json_file:
        parameters = json.load(json_file)
        for param in parameters:
            logging.debug('Parameter {} is {}'.format(param, parameters[param]))

    agent_pars = {}
    for par_name in ['banks', 'households', 'firms', 'central-bank']:
        par_path = os.path.join(input_folder_path, par_name)
        par_files = os.listdir(par_path)
        i_pars = []
        for file in par_files:
            with open(os.path.join(par_path, file)) as json_file:
                individual_parameters = json.load(json_file)
            i_pars.append(individual_parameters)

        agent_pars[par_name] = i_pars

    # load network from file
    network_path = os.path.join(input_folder_path, 'network.gexf')
    graph = nx.read_gexf(network_path)

    # 2 initialisation
    environment = Environment(parameters, agent_pars['banks'], agent_pars['households'],
                              agent_pars['firms'], agent_pars['central-bank'], graph)

    if kwargs.get('output_folder_path'):
        output_folder_path = kwargs.get('output_folder_path')
    else:
        output_folder_path = os.getcwd()

    # check if the output folder path exists. If not create it:
    if not os.path.isdir(output_folder_path):
        os.makedirs(output_folder_path)
        click.echo('Created output folder at {}'.format(output_folder_path))

    # 3 simulate the model and return an updated environment
    environment = runner(environment, **kwargs)

    # 4 measurement
    pd.DataFrame(environment.measurement).to_csv(os.path.join(output_folder_path, 'simple_output.csv'), sep=';')
    click.echo('Simulation done, check out the output data here: {}'.format(output_folder_path))


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("CBDC-simulation")
    main()
