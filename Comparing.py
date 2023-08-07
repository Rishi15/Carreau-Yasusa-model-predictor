import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Import necessary libraries

# Step 2: Read data from Excel sheets into Pandas DataFrames
df1 = pd.read_excel('C:\Users\z004r5jk\Desktop\Viscosity_Comparison.xlsx', sheet_name='CFD')
df2 = pd.read_excel('C:\Users\z004r5jk\Desktop\Viscosity_Monitor_2_Plot_data_00121.csv', sheet_name='Sheet1')

# Step 3: Extract X and Y values for each graph
x1 = df1['Shear Rate']
y1 = df1['Viscosity']
x2 = df2['Shear Rate']
y2 = df2['Viscosity Monitor 2: Viscosity Monitor 2 (Pa-s)']

# Step 4: Create Matplotlib figure and axes
fig, ax = plt.subplots()

# Step 5: Plot the first graph
ax.plot(x1, y1, label='Graph 1')

# Step 6: Plot the second graph
ax.plot(x2, y2, label='Graph 2')

# Step 7: Customize the chart
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Two XY Graphs')
ax.legend()

# Step 8: Display the chart
plt.show()