# Load the new data from the CSV file
leaf_data = pd.read_csv(leaf_file_path)

# Display the first few rows to understand its structure
leaf_data.head()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the new data from the CSV file
leaf_file_path = '/mnt/data/leaf.csv'
leaf_data = pd.read_csv(leaf_file_path)

# Define a function to create and save boxplots with colons in variable names
def create_save_boxplot_with_colon(variable, data, folder_path='/mnt/data/'):
    # Replace special characters for filename compatibility
    file_variable_name = variable.replace("[", "").replace("]", "").replace("/", "_").replace(":", "_")
    
    # Create a boxplot for the given variable
    plt.figure(figsize=(15, 10))
    boxplot = sns.boxplot(x='Strain', y=variable, hue='Variant', data=data, palette="Set3")
    boxplot.set_xlabel('Strain', fontsize=14)
    boxplot.set_ylabel(variable, fontsize=14)
    plt.xticks(rotation=45)  # Rotate the x labels to make them readable
    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    
    # Save the plot to a PNG file
    file_name = f'{folder_path}{file_variable_name}_boxplot.png'
    plt.savefig(file_name)
    plt.close()  # Close the plot to avoid display
    
    return file_name

# List of variables to create boxplots for, with colons included in names as requested
variables_with_colons = [
    'Fe[mg/kg]', 'Cu[mg/kg]', 'Zn[mg/kg]', 'K[mg/kg]', 'Mg[mg/kg]',
    'Ca[mg/kg]', 'Na[mg/kg]', 'Mn[mg/kg]', 'P[mg/kg]', 'Ca:P', 
    'Fe:Mn', 'K:Ca', 'K:Mg', 'Ca:Mg', 'K:[Ca+Mg]'
]

# Create and save boxplots for all variables with colons in their names
png_files_with_colons = []
for variable in variables_with_colons:
    # Check if the variable requires calculation
    if ':' in variable or '[' in variable:
        # Calculate the new column if it does not exist
        elements = variable.replace('[', '').replace(']', '').split(':')
        if len(elements) == 2 and all(elem in leaf_data.columns for elem in elements):
            leaf_data[variable] = leaf_data[elements[0]] / leaf_data[elements[1]]
    # Create and save the boxplot
    if variable in leaf_data.columns:  # Ensure the variable is in the dataframe
        file_path = create_save_boxplot_with_colon(variable, leaf_data)
        png_files_with_colons.append(file_path)
