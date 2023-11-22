# Define a function to create and save boxplots for each variable
def create_save_boxplot(variable, data, variant='Variant', strain='Strain', folder_path='/mnt/data/'):
    # Create a boxplot for the given variable
    plt.figure(figsize=(15, 10))
    boxplot = sns.boxplot(x=strain, y=variable, hue=variant, data=data, palette="Set3")
    boxplot.set_xlabel(strain, fontsize=14)
    boxplot.set_ylabel(variable, fontsize=14)
    plt.xticks(rotation=45)  # Rotate the x labels to make them readable
    plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
    
    # Save the plot to a PNG file
    file_name = f'{folder_path}{variable.replace(" ", "_").replace("[", "").replace("]", "").replace("/", "_")}_boxplot.png'
    plt.savefig(file_name)
    plt.close()  # Close the plot to avoid display
    
    return file_name

# Update the 'Salinity [mS/cm]' column by dividing by 1000
soil_data['Salinity [mS/cm]'] = soil_data['Salinity [mS/cm]'] / 1000

# List of variables to create boxplots for
variables = ['pH in KCl', 'pH in H2O', 'Salinity [mS/cm]', 'Organic matter [%]', 'Mg [mg/kg]',
             'K [mg/kg]', 'Fe [mg/kg]', 'Mn [mg/kg]', 'Zn [mg/kg]', 'Cu [mg/kg]', 'P [mg/100g]']

# Create and save boxplots for all variables
png_files = []
for variable in variables:
    file_path = create_save_boxplot(variable, soil_data)
    png_files.append(file_path)

png_files  # Display the paths to the saved PNG files
