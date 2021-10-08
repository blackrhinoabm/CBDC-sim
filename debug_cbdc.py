# To use this script comment out the @click decorators in the __main__ and place input & output folders in root
import pandas as pd
from cbdcsim.__main__ import brsolow



brsolow(time= 188, input_folder_path='input',  output_folder_path='output')



