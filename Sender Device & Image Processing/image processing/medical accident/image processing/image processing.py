import cv2
import numpy as np
import time

def realtime_people_counter():
    # Initialize HOG descriptor for people detection
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    # For FPS calculation
    prev_time = time.time()
    
    while True:
        # Capture frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame")
            break
            
        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        
        # Resize frame for faster detection
        frame_resized = cv2.resize(frame, (640, 480))
        
        try:
            # Detect people
            boxes, weights = hog.detectMultiScale(
                frame_resized,
                winStride=(4, 4),
                padding=(8, 8),
                scale=1.05
            )
            
            # Draw boxes around detected people
            person_count = len(boxes)
            
            # Draw boxes and confidence scores
            for (x, y, w, h), conf in zip(boxes, weights):
                # Scale coordinates back to original frame size
                scale_x = frame.shape[1] / frame_resized.shape[1]
                scale_y = frame.shape[0] / frame_resized.shape[0]
                
                x = int(x * scale_x)
                y = int(y * scale_y)
                w = int(w * scale_x)
                h = int(h * scale_y)
                
                # Draw rectangle and confidence score
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                conf_text = f'{conf:.2f}'
                cv2.putText(frame, conf_text, (x, y-10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
        except Exception as e:
            print(f"Detection error: {str(e)}")
            person_count = 0
        
        # Add information to frame
        cv2.putText(frame, f'People count: {person_count}', (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f'FPS: {fps:.1f}', (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Display frame
        cv2.imshow('People Counter', frame)
        
        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    realtime_people_counter()
