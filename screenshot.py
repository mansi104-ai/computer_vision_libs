import cv2
import os

# Set the path to the folder where you want to save the screenshot
folder_path = "C:\Users\mansi\machine_learning\computer_vision_libs\computer_vision_libs\"
# Open the first available camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error opening video capture.")
    exit()

# Create a window to display the camera feed
cv2.namedWindow("Camera Feed")

while True:
    # Read frame from the camera
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error reading frame from video capture.")
        break

    # Display the frame in the window
    cv2.imshow("Camera Feed", frame)

    # Check for key press to take a screenshot
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Construct the file path for saving the screenshot
        file_path = os.path.join(folder_path, "screenshot.png")

        # Save the screenshot
        cv2.imwrite(file_path, frame)
        print("Screenshot saved at:", file_path)
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()