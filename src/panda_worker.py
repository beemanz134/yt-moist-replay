import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks

# area chart image dimension
# 40 px y
# 838 px x
#3188 seconds

# def get_datap(duration):
#     total_seconds = duration
total_seconds = 3188
image = cv2.imread('rsrc/output_image.png', cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)

# Display the binary image for verification
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')
plt.axis('off')

# Get dimensions
height = binary_image.shape[0]  # Should be 40
width = binary_image.shape[1]   # Should be 838

# Initialize y_values
y_values = np.zeros(width)

# Extract maximum heights
for x in range(width):
    if np.any(binary_image[:, x] == 255):
        max_y = np.max(np.where(binary_image[:, x] == 255)[0])
        y_values[x] = height - max_y
    else:
        y_values[x] = 0

# Normalize y_values
y_values_normalized = (y_values / height) * 100

# Detect peaks
peaks, _ = find_peaks(y_values_normalized, height=0)

# Calculate time per pixel
time_per_pixel = total_seconds / width

# Create DataFrame for peaks with time in seconds
peaks_df = pd.DataFrame({
    'x_coordinate_seconds': peaks * time_per_pixel,
    'y_value': y_values_normalized[peaks]
})

# Print the peaks DataFrame
print(peaks_df)

# Initialize lists for beginning and end points
beginning_points = []
end_points = []

threshold = 0.5
for peak in peaks:
    # Find the beginning point (rise)
    beginning_found = False
    for i in range(peak, 0, -1):
        if y_values_normalized[i] < y_values_normalized[peak] - threshold:
            beginning_points.append((i + 1) * time_per_pixel)  # Convert to seconds
            beginning_found = True
            break
    if not beginning_found:
        beginning_points.append(0)  # If no rise found, append 0

    # Find the end point (fall)
    end_found = False
    for i in range(peak, len(y_values_normalized) - 1):
        if y_values_normalized[i] < y_values_normalized[peak] - threshold:
            end_points.append(i * time_per_pixel)  # Convert to seconds
            end_found = True
            break
    if not end_found:
        end_points.append(total_seconds)  # If no fall found, append total seconds

# Create a DataFrame to store the results
rise_fall_df = pd.DataFrame({
    'peak_x_coordinate_seconds': peaks * time_per_pixel,
    'beginning_point_seconds': beginning_points,
    'end_point_seconds': end_points
})

# Print the rise and fall DataFrame
print(rise_fall_df)
plt.close()
# return rise_fall_df


