# Email: 23f2002999@ds.study.iitm.ac.in

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt

# __Cell 1: Interactive Widget__
# Define an interactive slider. Its value (`num_points_slider.value`) is
# automatically available to other cells.
num_points_slider = mo.ui.slider(
    start=20, stop=250, step=10, value=100, label="Number of data points:"
)


# __Cell 2: Dynamic Markdown Output__
# This cell depends on `num_points_slider` from Cell 1.
# The f-string dynamically updates the markdown text whenever the
# slider's value changes, providing self-documenting output.
md_output = mo.md(
    f"""
    ## 📊 Interactive Data Relationship
    
    This notebook demonstrates a simple reactive analysis.
    Adjust the slider below to change the number of points generated and plotted.
    
    - **Current number of points selected:** **{num_points_slider.value}**
    
    {num_points_slider}
    """
)


# __Cell 3: Data Generation__
# This cell has a dependency on `num_points_slider` from Cell 1.
# The variables `x` and `y` are recalculated every time the slider is adjusted,
# triggering any downstream cells (like the plot in Cell 4) to re-run.
num_points = num_points_slider.value
np.random.seed(42) # for reproducibility
x = np.linspace(0, 10, num_points)
y = 2 * x + 1 + np.random.normal(0, 2, num_points)


# __Cell 4: Data Visualization__
# This cell depends on the `x` and `y` variables from Cell 3.
# The plot is automatically redrawn with the new data whenever
# the slider's value is changed.
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.7, label=f'{num_points} data points')
ax.set_title("Relationship between X and Y")
ax.set_xlabel("Independent Variable (X)")
ax.set_ylabel("Dependent Variable (Y)")
ax.grid(True)
ax.legend()


# __Cell 5: Final Layout__
# This cell arranges the final app layout by displaying the outputs from
# the markdown (Cell 2) and the plot (Cell 4).
mo.vstack([md_output, fig])