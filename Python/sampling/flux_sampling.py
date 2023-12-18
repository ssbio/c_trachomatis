import cobra
from cobra.sampling import sample
import pandas as pd

# Load the model from a file in SBML format
model = cobra.io.read_sbml_model("C:/Users/niazc/OneDrive/Desktop/iCTB278.xml")

# Sampling analysis
s = sample(model, 500)

# Create a DataFrame from the sample results
df = pd.DataFrame(s)

# Write the DataFrame to an Excel file
with pd.ExcelWriter('sample_results.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sample Results')