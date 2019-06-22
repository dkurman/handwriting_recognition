import sys
sys.path.append('./text_segmentation/darkflow_recognition_tool/')
sys.path.append('./word_recognition/SimpleHTRKazPost/src/')
import objects_detector as rt
import img2text as it
import cv2

span = 5
def recognize_words(imagename):
    result, image = rt.obj_detector(imagename)
    word_prob = []
    for res in result:
        if res['label'] != 'word':
            continue
        x = res['topleft']['x']
        y = res['topleft']['y']
        width = res['bottomright']['x'] - x
        height = res['bottomright']['y'] - y
        cropped = image[y-span:y+height+span, x-span:x+width+span, :]
        word, prob = it.img2text(cropped)
        word_prob.append((word, prob))
        filename = f"output/{word}_{round(prob, 4)}.jpg"
        cv2.imwrite(filename, cropped)   
    print(word_prob)

