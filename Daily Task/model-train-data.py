import math
from openpyxl import Workbook
import numpy as np

# Step 1: Generate 500 x values from 0 to π (in radians)
x_values = np.linspace(0, math.pi, 500)

# Step 2: Create new Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "XY_Radians"

# Step 3: Write headers
ws.append(["x", "y"])

# Step 4: Calculate y values and write to sheet
for x in x_values:
    y = x * math.sin(x) + x * math.cos(x)
    ws.append([x, y])

# Step 5: Save Excel file
wb.save("data.xlsx")

print("✅ Excel file 'data.xlsx' created successfully with 500 data points!")
