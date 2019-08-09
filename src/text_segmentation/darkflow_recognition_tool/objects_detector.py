from darkflow.net.build import TFNet
import cv2

def obj_detector(img_name, thresh = 0.3): 
    img  = cv2.imread(img_name) 
    options = {
    'model': 'text_segmentation/darkflow_recognition_tool/model/yolo-post.cfg',
    'load': 'text_segmentation/darkflow_recognition_tool/model/yolo-post_6900.weights',
    'threshold': thresh,
    'gpu': 0.5,
    'labels': 'text_segmentation/darkflow_recognition_tool/model/post.names'
    }
    tfnet = TFNet(options)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (1000,800), interpolation = cv2.INTER_AREA)
    result = tfnet.return_predict(img)
    # for res in result:
    #     tl = (res['topleft']['x'], res['topleft']['y'])
    #     br = (res['bottomright']['x'], res['bottomright']['y'])
    #     label = res['label']
    #     if label == 'word':
    #         img = cv2.rectangle(img, tl, br, (255, 0, 0), 1)
    #         img = cv2.putText(img, "w", (res['topleft']['x'], res['topleft']['y'] - 5), cv2.FONT_HERSHEY_COMPLEX, 0.35, (255, 0, 0), 1)
    #     elif label == 'empty':
    #         img = cv2.rectangle(img, tl, br, (0, 255, 0), 1)
    #         img = cv2.putText(img, "t:2", (res['topleft']['x'], res['topleft']['y'] - 5), cv2.FONT_HERSHEY_COMPLEX, 0.35, (0, 255, 0), 1) 
       

    return [result, img]

'''
if __name__ == "__main__":
    res = obj_detector('0.jpg')
    print(res)
'''
