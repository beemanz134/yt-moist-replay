import cv2
import numpy as np

def image_worker():
    x1, y1 = 37, 473  # Top-left corner
    x2, y2 = 875, 513  # Bottom-right corner

    image_path = "rsrc/screenshot.png"
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        exit()
    clone = image.copy()
    roi = clone[y1:y2, x1:x2]

    # base_name, ext = os.path.splitext(image_path)
    # cropped_image_path = f"{base_name}_cropped{ext}"
    # cv2.imwrite(cropped_image_path, roi)
    # print(f"Cropped image saved to: {cropped_image_path}")
    # cv2.destroyAllWindows()
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Define the range for red color in HSV
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = mask1 | mask2
    inverse_mask = cv2.bitwise_not(red_mask)

    result_image = cv2.bitwise_and(roi, roi, mask=inverse_mask)

    # Save or display the result
    cv2.imwrite('rsrc/output_image.png', result_image)
