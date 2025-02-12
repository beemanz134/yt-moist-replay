import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks

# area chart image dimension
# 40 px y
# 838 px x
#3188 seconds

# def get_datap():

seconds = 3188
image = cv2.imread('rsrc/output_image.png', cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)

# Display the binary image for verification
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')
plt.axis('off')


# Step 3: Get dimensions
height = binary_image.shape[0]  # Should be 40
width = binary_image.shape[1]   # Should be 838

# Step 4: Initialize y_values
y_values = np.zeros(width)

# Step 5: Extract maximum heights
for x in range(width):
    # Find the maximum y-value (height) for the current x-coordinate
    # We find the highest white pixel (255) in the binary image
    if np.any(binary_image[:, x] == 255):
        max_y = np.max(np.where(binary_image[:, x] == 255)[0])  # Get the index of the highest white pixel
        y_values[x] = height - max_y  # Calculate height from the bottom
    else:
        y_values[x] = 0  # If no white pixel, height is 0

# Step 6: Normalize y_values
y_values_normalized = (y_values / height) * 100  # Normalize to a scale of 0-100

# Step 7: Detect peaks
peaks, _ = find_peaks(y_values_normalized, height=0)  # Adjust height if needed

# Step 8: Create DataFrame
peaks_df = pd.DataFrame({
    'x_coordinate': peaks,
    'y_value': y_values_normalized[peaks]
})

# Print the peaks DataFrame
print(peaks_df)


plt.close()
