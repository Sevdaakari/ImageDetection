import cv2
from django.shortcuts import render, redirect
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import numpy as np
import appUI.views as views

# Load Clip model & Processor
model_id = 'openai/clip-vit-base-patch32'
processor = CLIPProcessor.from_pretrained(model_id)
model = CLIPModel.from_pretrained(model_id)

def detect_object(image):
    # Get image
    img_path = f"{image}"
    img = cv2.imread(img_path)
    print(f'image shape: {img.shape}')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (224, 224)) # matching Clip input size
    img_pil = Image.fromarray(img_resized)

    # Encode image
    inputs = processor(text=None, images=img_pil, return_tensors="pt", padding=True)
    with torch.no_grad():
        img_features = model.get_image_features(**inputs)


    #Object detection using YOLOv3
    net = cv2.dnn.readNet("./appUI/yolov3.weights", "./appUI/yolov3.cfg")
    classes = []
    with open("./appUI/coco.names", "r") as coco:
        classes = coco.read().splitlines()

    blob = cv2.dnn.blobFromImage(img_rgb, 1/255, (416, 416), (0, 0, 0), True, crop=False)   
    # Explained params for above line: 
    # 1/255 scales the pixel values of the image, dividing by 255 normalizes these values to the range 0 to 1
    # 416, 416 will resize input image as YOLOv3 was trained on images of size 416x416 pixels
    # 0, 0, 0 is mean values, no mean subtraction is performed in our case
    # True - image should be swapped from BGR to RGB
    # False -  means that the entire image will be retained after resizing


    # Process the output of the YOLOv3 model
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.5:
                center_x = int(detection[0] * img_rgb.shape[1])
                center_y = int(detection[1] * img_rgb.shape[0])
                w = int(detection[2] * img_rgb.shape[1])
                h = int(detection[3] * img_rgb.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(f'indexes: {indexes}')

    # Visually annotate the detected objects in the image by drawing bounding boxes around them and adding text labels indicating their names
    font = cv2.FONT_HERSHEY_PLAIN
    colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]
    detected_objects = []

    if len(indexes) > 0:
        for index in indexes.flatten():
            x, y, w, h = boxes[index]
            label = str(classes[class_ids[index]])
            color = colors[index % 3]
            detected_objects.append({"name": classes[class_ids[index]], "confidence": confidences[index]})
            cv2.rectangle(img_rgb, (x, y), (x +w, y + h), color, 2)
            cv2.putText(img_rgb, label, (x, y + 30), font, 3, color, 3)

    # Resize output image for python view in case if it's too large
    # max_height = 1000
    # max_width = 1400
    # height, width, _ = img_rgb.shape
    # if height > max_height or width > max_width:
    #     scale = min(max_height / height, max_width / width)
    #     img_rgb = cv2.resize(img_rgb, (int(width * scale), int(height * scale)))

    # Display results via python
    # cv2.imshow("Detected objects ", img_rgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return detected_objects  

