import cv2

# Open the first available camera
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video capture.")
    exit()

# Create a window to display the camera feed
cv2.namedWindow("Camera Feed")

while True:
    # Read frame from the camera
    ret, frame = cap.read()

    # Check if frame was read successfully
    if not ret:
        print("Error reading frame from video capture.")
        break

    # Display the frame in the window
    cv2.imshow("Camera Feed", frame)

    # Check for key press to take a screenshot
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the screenshot
        cv2.imwrite("screenshot.png", frame)
        print("Screenshot saved as screenshot.png.")
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()