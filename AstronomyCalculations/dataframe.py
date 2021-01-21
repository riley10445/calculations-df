import pandas as pd
from planet_data import names
from planet_data import synodic_periods
from planet_data import greatest_elongation_angles
from planet_data import quarter_periods
from main import solar_distances
from main import sidereal_periods

# data_to_dataframe()
# Create initial Pandas data frame from planet names
planets_data = pd.DataFrame(names, columns=['Planet'])

# Append synodic periods to planets_data data frame
planets_data['Synodic Period'] = synodic_periods

# Append "quarter periods" to planets_data data frame
planets_data['Quarter Period'] = quarter_periods

planets_data['Greatest Elongation'] = greatest_elongation_angles

planets_data['Sidereal Period'] = sidereal_periods

planets_data['Solar Distance'] = solar_distances
