import sqlite3
import pandas as pd
import plotly.graph_objects as go

def plot_bmi_data():
    # connect to database
    conn = sqlite3.connect('.././database/master.db')
    df = pd.read_sql_query("SELECT bmi FROM bmi", conn)

    # Create a Plotly figure
    fig = go.Figure()

    # Add a trace to the figure
    fig.add_trace(go.Histogram(x=df['bmi'], nbinsx=50))

    # Set the title of the plot
    fig.update_layout(title_text='BMI Distribution')

    # Return the plot
    return fig