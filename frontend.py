import cv2

def open_camera_and_capture_photo(camera_index=0, output_file="captured_photo.jpg"):
    # Open the specified camera
    cap = cv2.VideoCapture(camera_index)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture a frame.")
            break

        # Display the frame
        cv2.imshow("Camera", frame)

        # Press 'c' to capture a photo
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite(output_file, frame)
            print(f"Photo captured and saved as {output_file}")
            
            # Display the captured image
            captured_image = cv2.imread(output_file)
            cv2.imshow("Captured Image", captured_image)
            cv2.waitKey(0)  # Wait for a key press to close the captured image window
            break

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

open_camera_and_capture_photo()
