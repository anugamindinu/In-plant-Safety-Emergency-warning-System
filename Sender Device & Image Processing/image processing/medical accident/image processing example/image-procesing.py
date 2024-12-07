# import cv2
# import numpy as np

# # Load YOLO model for object detection
# net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Add correct paths
# layer_names = net.getLayerNames()
# output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# # Load class labels (e.g., people, injuries, etc.)
# classes = []
# with open("coco.names", "r") as f:  # Add correct path
#     classes = [line.strip() for line in f.readlines()]

# # Initialize webcam (default camera is index 0)
# cap = cv2.VideoCapture(0)  # 0 opens the laptop's default webcam
# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# print("Press 'q' to quit the application.")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame.")
#         break

#     height, width, channels = frame.shape

#     # Pre-process the frame
#     blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Analyze the detections
#     class_ids, confidences, boxes = [], [], []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:  # Adjust threshold
#                 # Object detected
#                 center_x, center_y = int(detection[0] * width), int(detection[1] * height)
#                 w, h = int(detection[2] * width), int(detection[3] * height)
#                 x, y = int(center_x - w / 2), int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply Non-Maximum Suppression to avoid duplicate boxes
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#     # Draw bounding boxes and labels
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             confidence = confidences[i]
#             color = (0, 255, 0)  # Green for bounding box
#             cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#             # Trigger action if "person" or relevant class detected
#             if label == "person":
#                 print("Person detected! (Confidence: {:.2f})".format(confidence))
#                 # Add IoT integration for sending alerts

#     # Display the frame
#     cv2.imshow("Real-Time Detection", frame)

#     # Exit on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import numpy as np

# # Load YOLO model for object detection
# net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Add correct paths
# layer_names = net.getLayerNames()
# output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# # Load class labels (e.g., people, injuries, etc.)
# classes = []
# with open("coco.names", "r") as f:  # Add correct path
#     classes = [line.strip() for line in f.readlines()]

# # Initialize webcam (default camera is index 0)
# cap = cv2.VideoCapture(0)  # 0 opens the laptop's default webcam
# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# print("Press 'q' to quit the application.")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame.")
#         break

#     height, width, channels = frame.shape

#     # Pre-process the frame
#     blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Analyze the detections
#     class_ids, confidences, boxes = [], [], []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:  # Adjust threshold
#                 # Object detected
#                 center_x, center_y = int(detection[0] * width), int(detection[1] * height)
#                 w, h = int(detection[2] * width), int(detection[3] * height)
#                 x, y = int(center_x - w / 2), int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply Non-Maximum Suppression to avoid duplicate boxes
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#     # Count the number of "person" detections
#     person_count = 0
#     for i in range(len(boxes)):
#         if i in indexes:
#             label = str(classes[class_ids[i]])
#             if label == "person":
#                 person_count += 1

#     # Draw bounding boxes and labels
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             confidence = confidences[i]
#             color = (0, 255, 0)  # Green for bounding box
#             cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#     # Display the person count on the frame
#     cv2.putText(frame, f"Persons detected: {person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#     # Check for gatherings
#     if person_count > 3:  # Adjust threshold for a "gathering"
#         cv2.putText(frame, "Accident occurred!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
#         print("Accident occurred!")

#     # Display the frame
#     cv2.imshow("Real-Time Detection", frame)

#     # Exit on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
 
#  /////////////////////

# import cv2
# import numpy as np
# import pygame  # Import pygame for playing sound

# # Load YOLO model for object detection
# net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Add correct paths
# layer_names = net.getLayerNames()
# output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# # Load class labels (e.g., people, injuries, etc.)
# classes = []
# with open("coco.names", "r") as f:  # Add correct path
#     classes = [line.strip() for line in f.readlines()]

# # Initialize webcam (default camera is index 0)
# cap = cv2.VideoCapture(0)  # 0 opens the laptop's default webcam
# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# print("Press 'q' to quit the application.")

# # Initialize pygame for alarm sound
# pygame.mixer.init()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame.")
#         break

#     height, width, channels = frame.shape

#     # Pre-process the frame
#     blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Analyze the detections
#     class_ids, confidences, boxes = [], [], []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:  # Adjust threshold
#                 # Object detected
#                 center_x, center_y = int(detection[0] * width), int(detection[1] * height)
#                 w, h = int(detection[2] * width), int(detection[3] * height)
#                 x, y = int(center_x - w / 2), int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply Non-Maximum Suppression to avoid duplicate boxes
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#     # Count the number of "person" detections
#     person_count = 0
#     for i in range(len(boxes)):
#         if i in indexes:
#             label = str(classes[class_ids[i]])
#             if label == "person":
#                 person_count += 1

#     # Draw bounding boxes and labels
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             confidence = confidences[i]
#             color = (0, 255, 0)  # Green for bounding box
#             cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#     # Display the person count on the frame
#     cv2.putText(frame, f"Persons detected: {person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#    # Check for gatherings (number of people threshold)
#     if person_count > 1:  # Adjust threshold for a "gathering"
#         cv2.putText(frame, "Accident occurred!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
#         print("Accident occurred!")

#         # Trigger alarm sound when a gathering is detected
#         pygame.mixer.init()
#         pygame.mixer.music.load("alarm_sound.mp3")  # Load your alarm sound file
#         pygame.mixer.music.play(loops=0)  # Play the sound once

#     # Display the frame
#     cv2.imshow("Real-Time Detection", frame)
    
#     # Initialize and play the alarm sound
#     pygame.mixer.music.load("alarm_sound.mp3")  # Load your alarm sound file
#     pygame.mixer.music.play(loops=0)  # Play the sound once


#     # Display the frame
#     cv2.imshow("Real-Time Detection", frame)

#     # Exit on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# ///////////////////////////////

# import cv2
# import numpy as np
# import pygame  # To play sound for the alarm

# # Load YOLO model for object detection
# net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Add correct paths
# layer_names = net.getLayerNames()
# output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# # Load class labels (e.g., people, injuries, etc.)
# classes = []
# with open("coco.names", "r") as f:  # Add correct path
#     classes = [line.strip() for line in f.readlines()]

# # Initialize webcam (default camera is index 0)
# cap = cv2.VideoCapture(0)  # 0 opens the laptop's default webcam
# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# print("Press 'q' to quit the application.")

# # Main loop for real-time detection
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame.")
#         break

#     height, width, channels = frame.shape

#     # Pre-process the frame
#     blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Analyze the detections
#     class_ids, confidences, boxes = [], [], []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:  # Adjust threshold
#                 # Object detected
#                 center_x, center_y = int(detection[0] * width), int(detection[1] * height)
#                 w, h = int(detection[2] * width), int(detection[3] * height)
#                 x, y = int(center_x - w / 2), int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply Non-Maximum Suppression to avoid duplicate boxes
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#     # Count the number of "person" detections
#     person_count = 0
#     for i in range(len(boxes)):
#         if i in indexes:
#             label = str(classes[class_ids[i]])
#             if label == "person":
#                 person_count += 1

#     # Draw bounding boxes and labels
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             confidence = confidences[i]
#             color = (0, 255, 0)  # Green for bounding box
#             cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#     # Display the person count on the frame
#     cv2.putText(frame, f"Persons detected: {person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#     # Check for gatherings (number of people threshold)
#     if person_count > 1:  # Adjust threshold for a "gathering"
#         cv2.putText(frame, "Accident occurred!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
#         print("Accident occurred!")

#         # Trigger alarm sound when a gathering is detected
#         pygame.mixer.init()
#         pygame.mixer.music.load("alarm_sound.mp3")  # Load your alarm sound file
#         pygame.mixer.music.play(loops=0)  # Play the sound once

#     # Display the frame
#     cv2.imshow("Real-Time Detection", frame)

#     # Exit on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and close the windows
# cap.release()
# cv2.destroyAllWindows()
# //////////////////////////////////

import cv2
import numpy as np
import pygame  # To play sound for the alarm

# Load YOLO model for object detection
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Add correct paths
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load class labels (e.g., people, injuries, etc.)
classes = []
with open("coco.names", "r") as f:  # Add correct path
    classes = [line.strip() for line in f.readlines()]

# Initialize webcam (default camera is index 0)
cap = cv2.VideoCapture(0)  # 0 opens the laptop's default webcam
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set the threshold for the number of people for triggering the alarm
threshold = 1

# Initialize variables
person_count = 0
alarm_playing = False

print("Press 'q' to quit the application.")

# Main loop for real-time detection
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    height, width, channels = frame.shape

    # Pre-process the frame
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Analyze the detections
    class_ids, confidences, boxes = [], [], []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Adjust threshold
                # Object detected
                center_x, center_y = int(detection[0] * width), int(detection[1] * height)
                w, h = int(detection[2] * width), int(detection[3] * height)
                x, y = int(center_x - w / 2), int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Maximum Suppression to avoid duplicate boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Count the number of "person" detections
    current_person_count = 0
    for i in range(len(boxes)):
        if i in indexes:
            label = str(classes[class_ids[i]])
            if label == "person":
                current_person_count += 1

    # Draw bounding boxes and labels
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)  # Green for bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the person count on the frame
    cv2.putText(frame, f"Persons detected: {current_person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Check for gatherings (number of people threshold)
    if current_person_count > threshold and not alarm_playing:  # Only play alarm if it's not already playing
        cv2.putText(frame, "Accident occurred!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        print("Accident occurred!")

        # Trigger alarm sound when a gathering is detected
        pygame.mixer.init()
        pygame.mixer.music.load("alarm_sound.mp3")  # Load your alarm sound file
        pygame.mixer.music.play(loops=0)  # Play the sound once
        alarm_playing = True  # Set the alarm as playing

    elif current_person_count <= threshold and alarm_playing:  # Stop the alarm if person count is below threshold
        pygame.mixer.music.stop()  # Stop the alarm sound
        alarm_playing = False  # Set the alarm as not playing

    # Display the frame
    cv2.imshow("Real-Time Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()
