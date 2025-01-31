import cv2
import os

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

    base_name, ext = os.path.splitext(image_path)
    cropped_image_path = f"{base_name}_cropped{ext}"
    cv2.imwrite(cropped_image_path, roi)
    print(f"Cropped image saved to: {cropped_image_path}")
    cv2.destroyAllWindows()
