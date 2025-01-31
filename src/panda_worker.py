import cv2
import numpy as np
import pandas as pd

# def get_datap:
# Step 1: Read the image
image = cv2.imread('rsrc/screenshot_cropped.png')

# Step 2: Preprocess the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)  # Invert colors if necessary

# Step 3: Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 4: Extract data points
data_points = []
for contour in contours:
    # Filter contours based on area or other criteria if necessary
    if cv2.contourArea(contour) > 100:  # Adjust this threshold as needed
        for point in contour:
            x, y = point[0]
            data_points.append((x, y))

# Step 5: Map coordinates to data points
# Define the ranges for the axes
x_min, x_max = 0, 100  # X-axis range
y_min, y_max = 0, 1000  # Y-axis range

# Calculate the scale factors
x_scale = (x_max - x_min) / image.shape[1]  # Scale for x-axis
y_scale = (y_max - y_min) / image.shape[0]  # Scale for y-axis

# Map pixel coordinates to actual data points
mapped_data_points = [(x * x_scale, y * y_scale) for x, y in data_points]

# Step 6: Store data in Pandas DataFrame
df = pd.DataFrame(mapped_data_points, columns=['X', 'Y'])

# Optionally, save the DataFrame to a CSV file
df.to_csv('extracted_data_points.csv', index=False)

# Display the DataFrame
print(df)
