[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python application](https://github.com/blackrhinoabm/sabcom/workflows/Python%20application/badge.svg)

![](https://cogeorg.github.io/images/black_rhino_logo.jpg)

 __Central Bank Digital Currency Transaction Simulator__

CBCD-sim is an open source, easy-to-use, agent-based, simulator of artificial monetary transactions

Currently the model can be run using debug_cbdc.py 

# Structure
The model uses the Black Rhino architecture in which the model is run from the __main__ file. The simularion order is: 

1. Load parameters from input/parameters.json
2. Initialise Environment class containing agents and measurements
3. Run the runner 
4. Which calls the updater
5. Which contains a time loop that for every period
6. Accrues from banks interest to the household and firm
7. For each transaction an entry is saved to the environment
8. At the end of the simulation the output is a csv file with all transactions (in output folder)

# Future / Click application
Once the model is finished the model can be downloaded using: 

    pip install cbdcsim

and then run using 

    cbdcsim simple <args>

# Disclaimer

This software is intended for educational and research purposes. Despite best efforts,
we cannot fully rule out the possibility of errors and bugs. The use of the CBDC simulator
is entirely at your own risk.
