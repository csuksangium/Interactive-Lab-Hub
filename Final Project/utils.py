import cv2
import numpy as np
from tflite_support.task import processor

_MARGIN = 10  # pixels
_ROW_SIZE = 25  # pixels
_FONT_SIZE = 3
_FONT_THICKNESS = 3
_TEXT_COLOR = (0, 0, 255)  # red

obj_list = ["scissors", "cup"]

def translation_dict(curr_lang, word):
    td = {"scissors": "scissors", "cup": "cup"}
    if curr_lang == "french":
        td = {"scissors": "les ciseaux", "cup": "la tasse"}
    elif curr_lang == "spanish":
        td = {"scissors": "las tijeras", "cup": "la copa"}
    return td[word]

def visualize(
    image: np.ndarray,
    detection_result: processor.DetectionResult,
    curr_lang
) -> np.ndarray:
  for detection in detection_result.detections:
      
    category = detection.categories[0]
    category_name = category.category_name
    
    if category_name not in obj_list:
        continue
    
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, _TEXT_COLOR, 3)

    # Draw label and score
    result_text = translation_dict(curr_lang, category_name)
    text_location = (_MARGIN + bbox.origin_x,
                     _MARGIN + _ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)

  return image
