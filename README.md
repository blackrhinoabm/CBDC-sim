[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python application](https://github.com/blackrhinoabm/sabcom/workflows/Python%20application/badge.svg)

![](https://cogeorg.github.io/images/black_rhino_logo.jpg)

 __Central Bank Digital Currency Transaction Simulator__

CBCD-sim is an open source, easy-to-use, agent-based, simulator of artificial monetary transactions

Currently the model can be run using debug_cbdc.py 

# Structure
The model uses the Black Rhino architecture in which the model is run from the __main__ file. To run the model two
folders are required: an input folder (containing general and agent specific input parameters) and an output folder
(where the transaction output csv will be stored).

The simulation order is: 

1. (optionally) Update the set-parameters notebook to change parameters in the input folder 
2. the model runs from the __main__.py file (used to make this run as a Click application)
3. Load parameters from input/parameters.json
4. Initialise Environment class containing agents and measurements
5. Run the runner 
6. Which calls the updater
7. Which contains a time loop that for every period
8. Accrues from banks interest to the household and firm
9. For each transaction an entry is saved to the environment
10. At the end of the simulation the output is a csv file with all transactions (in output folder)

# Changing how the model works 
The simplest way to change how the model works is by changing the parameters. For deeper structural changes
the most important logic of the model (day loop) happens in the updater.py file. You can change the simulation there.

# Future / Click application
Once the model is finished the model can be downloaded using: 

    pip install cbdcsim

and then run using 

    cbdcsim simple <args>

# Disclaimer

This software is intended for educational and research purposes. Despite best efforts,
we cannot fully rule out the possibility of errors and bugs. The use of the CBDC simulator
is entirely at your own risk.
