import cv2
import numpy as np
import time

# Adjusted lower and upper bounds for fire-like color ranges in HSV
lower_red = np.array([0, 120, 80])      # Adjusted lower bound (red)
upper_red = np.array([10, 255, 255])    # Upper bound (red)

lower_orange = np.array([10, 100, 150]) # Adjusted lower bound (orange)
upper_orange = np.array([25, 255, 255]) # Upper bound (orange)

lower_yellow = np.array([25, 150, 180]) # Increased lower bound (yellow)
upper_yellow = np.array([35, 255, 255]) # Upper bound (yellow)

# Initialize variables for optical flow
prev_frame = None  # To store the previous frame

def detect_fire(frame):
    """Function to detect fire-like colors in the frame based on given color ranges"""
    
    # Convert frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create masks for fire-like colors (red, orange, yellow)
    mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
    mask_orange = cv2.inRange(hsv_frame, lower_orange, upper_orange)
    mask_yellow = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)

    # Combine masks to cover all fire-like colors
    fire_mask = mask_red | mask_orange | mask_yellow
    
    # Apply morphological operations to remove noise
    fire_mask = cv2.erode(fire_mask, None, iterations=2)
    fire_mask = cv2.dilate(fire_mask, None, iterations=2)
    
    return fire_mask

def calculate_optical_flow(prev_gray, current_gray, fire_mask):
    """Calculate optical flow and combine it with the fire mask"""
    # Calculate dense optical flow using Farneback method
    flow = cv2.calcOpticalFlowFarneback(prev_gray, current_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    # Compute magnitude and angle of the flow
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    
    # Increase the optical flow threshold to eliminate background movement noise
    motion_mask = (mag > 3.0).astype(np.uint8)  # Increased threshold for stronger motion
    
    # Combine motion mask with fire mask
    motion_fire_mask = cv2.bitwise_and(fire_mask, fire_mask, mask=motion_mask)
    
    # Find contours of moving fire-like regions
    contours, _ = cv2.findContours(motion_fire_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return motion_fire_mask, contours

# Function to calculate fire power based on the area covered
def calculate_fire_power(covered_area, total_area):
    fire_percentage = (covered_area / total_area) * 100
    
    # Categorize fire power based on the percentage of area covered
    if fire_percentage < 5:
        fire_power = "Low"
    elif 5 <= fire_percentage < 20:
        fire_power = "Medium"
    else:
        fire_power = "High"
    
    return fire_power, fire_percentage

# Main function
def main():
    global prev_frame
    cap = cv2.VideoCapture(0)  # 0 is typically the default camera. If you have multiple cameras, try 1, 2, etc.

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open video file")
        return

    start_time = time.time()
    coverage_data = []

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldn't read frame")
            break

        # Resize frame for faster processing (optional)
        frame = cv2.resize(frame, (640, 480))

        # Convert frame to grayscale for optical flow
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # If there is no previous frame, initialize it
        if prev_frame is None:
            prev_frame = gray_frame
            continue

        # Detect fire-like regions in the frame
        fire_mask = detect_fire(frame)

        # Calculate optical flow and combine it with the fire mask
        motion_fire_mask, contours = calculate_optical_flow(prev_frame, gray_frame, fire_mask)

        # Only proceed if there are any contours found
        if contours:
            # Find the largest contour (fire region)
            largest_contour = max(contours, key=cv2.contourArea)

            # Filter out small contours by setting a minimum contour area threshold
            min_contour_area = 500  # You can adjust this threshold based on your video quality
            if cv2.contourArea(largest_contour) < min_contour_area:
                continue

            # Compute bounding box for the largest fire region
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Draw rectangle around the largest fire region
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Fire", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # Calculate total area of the frame and covered area
            total_area = frame.shape[0] * frame.shape[1]
            fire_area = w * h

            # Calculate fire power
            fire_power, fire_percentage = calculate_fire_power(fire_area, total_area)

            # Display the fire power and percentage on the frame
            cv2.putText(frame, f"Fire Power: {fire_power}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Covered Area: {fire_percentage:.2f}%", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Accumulate coverage data for averaging over time
            coverage_data.append(fire_percentage)

        # Update the previous frame
        prev_frame = gray_frame

        # Display the resulting frame
        cv2.imshow('Fire Detection with Improved Optical Flow', frame)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Check if 5 seconds have passed
        if elapsed_time > 5:
            # Calculate and display average coverage percentage
            if coverage_data:
                avg_coverage = np.mean(coverage_data)
                print(f"Average Fire Coverage over 5 seconds: {avg_coverage:.2f}%")
            # Reset start time and coverage data
            start_time = time.time()
            coverage_data = []

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()