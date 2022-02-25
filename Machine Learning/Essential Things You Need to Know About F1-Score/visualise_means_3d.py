# Import modules
import numpy as np
import pandas as pd
import plotly.express as px
from itertools import product

# Define functions to compute means
def compute_harmonic_mean(x, y):
    return (2*x*y)/(x+y)

def compute_arithmetic_mean(x, y):
    return (x+y)/2

def compute_geometric_mean(x, y):
    return (x*y)**0.5

# Generate precision and recall values between 0 and 1
precision = np.arange(0.05, 1.05, 0.05)
recall = np.arange(0.05, 1.05, 0.05)

# Compute means
harmonic_mean = [compute_harmonic_mean(x,y) for x, y in list(product(precision, recall))]
arithmetic_mean = [compute_arithmetic_mean(x,y) for x, y in list(product(precision, recall))]
geometric_mean = [compute_geometric_mean(x,y) for x, y in list(product(precision, recall))]

# Organise data in Pandas DataFrame
data = {'Precision': [x for x, _ in list(product(precision, recall))],
        'Recall': [y for _, y in list(product(precision, recall))],
        'Harmonic Mean': harmonic_mean, 
        'Arithmetic Mean': arithmetic_mean, 
        'Geometric Mean': geometric_mean}

df = pd.DataFrame(data)

# Reshape data for ease of visualisation using Plotly Express
df_reshaped = pd.melt(df, id_vars=["Precision", "Recall"], var_name="Type", value_name="Value")

# Create 3D scatter plot
fig = px.scatter_3d(df_reshaped, x='Precision', y='Recall', z='Value', 
                    color='Type', opacity=0.8, range_color='Type')
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.update_traces(marker_size=5)
fig.show()