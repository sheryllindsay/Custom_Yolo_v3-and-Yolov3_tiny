#please set the paths correctly
#if your using yolov3 pr yolov3_tiny copy the "yolov3_custom_last.weights", "yolov3_custom.cfg"
#to this location and the 'test.mp4'

#use Object-Detection-API to run yolov3 tf files


# import required packages

import cv2
import argparse
import numpy as np

# read class names from text file
classes = None
with open("obj.names", 'r') as f:
	classes = [line.strip() for line in f.readlines()]

# generate different colors for different classes 
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

# read pre-trained model and config file
net = cv2.dnn.readNet("yolov3_custom_last.weights", "yolov3_custom.cfg")

def detect(image):

	Width = image.shape[1]
	Height = image.shape[0]
	scale = 0.00392

	# create input blob 
	blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

	# set input blob for the network
	net.setInput(blob)

	# function to get the output layer names 
	# in the architecture
	def get_output_layers(net):
	    
		layer_names = net.getLayerNames()
	    
		output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

		return output_layers

	# function to draw bounding box on the detected object with class name
	def draw_bounding_box(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
            
		label = str(classes[class_id])

		temp=str(confidence)

		color = COLORS[class_id]

		cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

		cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
		cv2.putText(img, temp, (x-10,y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

	# run inference through the network
	# and gather predictions from output layers
	outs = net.forward(get_output_layers(net))

	# initialization
	class_ids = []
	confidences = []
	boxes = []
	conf_threshold = 0.8
	nms_threshold = 0.4

	# for each detetion from each output layer 
	# get the confidence, class id, bounding box params
	# and ignore weak detections (confidence < 0.5)
	for out in outs:
		for detection in out:
			scores = detection[5:]
			class_id = np.argmax(scores)
			confidence = scores[class_id]
			if confidence > 0.5:
				center_x = int(detection[0] * Width)
				center_y = int(detection[1] * Height)
				w = int(detection[2] * Width)
				h = int(detection[3] * Height)
				x = center_x - w / 2
				y = center_y - h / 2
				class_ids.append(class_id)
				confidences.append(float(confidence))
				boxes.append([x, y, w, h])

	# apply non-max suppression
	indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

	# go through the detections remaining
	# after nms and draw bounding box
	for i in indices:
		i = i[0]
		box = boxes[i]
		x = box[0]
		y = box[1]
		w = box[2]
		h = box[3]
			    
		draw_bounding_box(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))

	# display output image    
	cv2.imshow("object detection", image)

#cap = cv2.VideoCapture(0)
# caturing from test video
cap = cv2.VideoCapture('test.mp4')

# Check if camera opened successfully 
if (cap.isOpened()== False):  
	print("Error opening video  file") 
   
# Read until video is completed 
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
	ret, frame = cap.read() 
	if ret == True: 
		detect(frame)
	 
	if cv2.waitKey(25) & 0xFF == ord('q'): 
		break
    
