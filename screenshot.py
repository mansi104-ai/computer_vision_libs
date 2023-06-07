import cv2
import pyautogui
import pygetwindow as gw
import os
import numpy as np

# Set the title of the window you want to capture
window_title = "My Window"

# Set the path to the folder where you want to save the screenshot
folder_path = "COMPUTER_VISION_LIBS"

# Find the coordinates of the top-left corner and the width and height of the window
window_info = gw.getWindowsWithTitle(window_title)
x, y, width, height = window_info.left, window_info.top, window_info.width, window_info.height

# Create a screenshot region based on the window coordinates
screenshot_region = (x, y, width, height)

# Create a window to display the captured image
cv2.namedWindow("Window Capture")

while True:
    # Capture the screenshot of the specified window region
    screenshot = pyautogui.screenshot(region=screenshot_region)

    # Convert the screenshot to OpenCV format
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Display the captured image in the window
    cv2.imshow("Window Capture", frame)

    # Check for key press to save the screenshot
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Construct the file path for saving the screenshot
        file_path = os.path.join(folder_path, "screenshot.png")
        
        # Save the screenshot
        screenshot.save(file_path)
        print("Screenshot saved at:", file_path)
        break

# Close the window
cv2.destroyAllWindows()