import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks

# area chart image dimension
# 40 px y
# 838 px x
def seconds_to_hhmmss(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def get_datap(duration):
    total_seconds = duration
    image = cv2.imread('rsrc/output_image.png', cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)

    height = binary_image.shape[0]  # Should be 40
    width = binary_image.shape[1]   # Should be 838

    y_values = np.zeros(width)

    for x in range(width):
        if np.any(binary_image[:, x] == 255):
            max_y = np.max(np.where(binary_image[:, x] == 255)[0])
            y_values[x] = height - max_y
        else:
            y_values[x] = 0

    y_values_normalized = (y_values / height) * 100

    peaks, _ = find_peaks(y_values_normalized, height=0)

    time_per_pixel = total_seconds / width

    peaks_df = pd.DataFrame({
        'x_coordinate_seconds': peaks * time_per_pixel,
        'y_value': y_values_normalized[peaks]
    })

    beginning_points = []
    end_points = []

    threshold = 0.5
    for peak in peaks:
        beginning_found = False
        for i in range(peak, 0, -1):
            if y_values_normalized[i] < y_values_normalized[peak] - threshold:
                beginning_points.append((i + 1) * time_per_pixel)  # Convert to seconds
                beginning_found = True
                break
        if not beginning_found:
            beginning_points.append(0)

        end_found = False
        for i in range(peak, len(y_values_normalized) - 1):
            if y_values_normalized[i] < y_values_normalized[peak] - threshold:
                end_points.append(i * time_per_pixel)
                end_found = True
                break
        if not end_found:
            end_points.append(total_seconds)

    rise_fall_df = pd.DataFrame({
        'peak_x_coordinate_seconds': peaks * time_per_pixel,
        'beginning_point_seconds': beginning_points,
        'end_point_seconds': end_points
    })

    rise_fall_df['peak_x_coordinate_seconds'] = rise_fall_df['peak_x_coordinate_seconds'].apply(seconds_to_hhmmss)
    rise_fall_df['beginning_point_seconds'] = rise_fall_df['beginning_point_seconds'].apply(seconds_to_hhmmss)
    rise_fall_df['end_point_seconds'] = rise_fall_df['end_point_seconds'].apply(seconds_to_hhmmss)

    slopes_only_df = rise_fall_df[['beginning_point_seconds', 'end_point_seconds']]
    slopes_only_df.columns = ['rise  ', '  fall']

    # Print the rise and fall DataFrame
    print(rise_fall_df)
    plt.close()
    slopes_only_df.to_csv('rsrc/rise_fall_data.txt', sep='~', index=False)

