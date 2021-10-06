import sys
import click
#import pickle
import os
#import time
#import copy
#import logging
#import json
#import random
import pandas as pd
#import networkx as nx
import numpy as np
#from scipy.integrate import odeint
#from SALib.sample import latin

#from sabcom.runner import runner
#from sabcom.estimation import ls_model_performance, constrNM
#from sabcom.differential_equation_model import differential_equations_model
#from sabcom.environment import Environment
#from sabcom.helpers import generate_district_data


@click.group()
@click.version_option("1.0.0")
def main():
	"""
	An open source, easy-to-use-and-adapt, CBDC-simulation model.
	"""
	pass


@main.command()
@click.option('--labour_growth', '-g', type=float, required=True,
              help="proportional labour growth")
@click.option('--efficiency_growth', '-eg', type=float, required=True,
              help="proportional efficiency growth")
@click.option('--savings_rate', '-s', type=float, required=True,
              help="percentage of income saved")
@click.option('--depreciation_rate', '-dr', type=float, required=True,
              help="how quickly capital depreciates")
@click.option('--production_elasticity', '-pe', type=float, required=True,
              help="elasticity of production")
@click.option('--labour_zero', '-lz', type=float, required=True,
              help="initial labour")
@click.option('--efficiency_zero', '-ez', type=float, required=True,
              help="how quickly capital depreciates")
@click.option('--time', '-t', type=int, required=True,
              help="simulated periods")
@click.option('--capital_zero', '-cz', type=float, required=True,
              help="how quickly capital depreciates")
@click.option('--output_folder_path', '-o', type=click.Path(exists=True), required=True,
              help="All simulation output will be deposited here")
def solow(**kwargs):
	"""
    This function is used to run / simulate a differential equation version of the Solow Growth model.
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
	labour_growth = kwargs.get('labour_growth') # the labor-force L proportional growth rate (n)
	print('labour_growth = ', labour_growth)
	efficiency_growth = kwargs.get('efficiency_growth') # the labor-efficiency E proportional growth rate (g)
	print('efficiency_growth = ', efficiency_growth)
	savings_rate = kwargs.get('savings_rate') # the share of production Y that is saved and invested (s)
	print('savings_rate = ', savings_rate)
	depreciation_rate = kwargs.get('depreciation_rate') # the capital depreciation rate (δ)
	print('depreciation_rate = ', depreciation_rate)
	production_elasticity = kwargs.get('production_elasticity') # the elasticitiy of production Y with respect to capital θ
	print('production_elasticity = ', production_elasticity)
	labour_0 = kwargs.get('labour_zero') # labour force T=0 (L_0)
	print('labour_zero = ', labour_0)
	efficiency_0 = kwargs.get('efficiency_zero') # labour efficiency T=0 (E_0)
	print('efficiency_zero = ', efficiency_0)
	capital_0 = kwargs.get('capital_zero') # capital at T=0 (κ_0)
	print('capital_zero = ', capital_0)
	time = kwargs.get('time') # simulation time
	print('time = ', time)

	output_folder_path = kwargs.get('output_folder_path')
	
	# initialisation:
	solow_df = pd.DataFrame()
	labour = [labour_0]
	labour_efficiency = [efficiency_0]
	capital_intensity = [capital_0]
	production = []
	capital = []
	output_per_worker = []
	
	# determine labour force size, labour efficiency, and capital intensity over time
	for t in range(time):
		labour = labour + [labour[t]*np.exp(labour_growth)]
		labour_efficiency = labour_efficiency + [labour_efficiency[t] * np.exp(efficiency_growth)]
		capital_intensity = capital_intensity + [capital_intensity[t] * (1 + (savings_rate/capital_intensity[t] - (labour_growth+efficiency_growth+depreciation_rate))/(1+production_elasticity))]

	# determine production, capital, and output per worker    
	for t in range(time+1):
		production = production + [(capital_intensity[t]**production_elasticity)*labour[t]*labour_efficiency[t]]
		capital = capital + [(capital_intensity[t]*production[t])]
		output_per_worker = output_per_worker + [production[t]/labour[t]]
	
	# fill dataframe
	solow_df['labour'] = labour
	solow_df['labour_efficiency'] = labour_efficiency
	solow_df['capital_intensity'] = capital_intensity
	solow_df['production'] = production
	solow_df['capital'] = capital
	solow_df['output_per_worker'] = output_per_worker

	solow_df.to_csv(os.path.join(output_folder_path, 'solow_output.csv'), sep=';')
	
	click.echo('Simulation done, check out the output data here: {}'.format(output_folder_path))


if __name__ == '__main__':
	args = sys.argv
	if "--help" in args or len(args) == 1:
		print("CBDC-simulation")
	main()
