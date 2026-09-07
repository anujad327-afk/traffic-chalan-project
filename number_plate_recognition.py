import cv2
from paddleocr import PaddleOCR
def num_plt():
    img = cv2.imread(r'no_parking1.jpg')
    x,y,w,h =528,667,133,44
    y2=y+h
    x2=x+w
    plate = img[y:y2,x:x2]

    plate=cv2.copyMakeBorder(plate,10,15,10,15,cv2.BORDER_CONSTANT)
    plate=cv2.resize(plate,(306,102),interpolation=cv2.INTER_CUBIC)

    cv2.imwrite('number_plate.jpg',plate)
    # cv2.imshow('number_plate.jpg',plate)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    ocr = PaddleOCR(lang='en')
    result=ocr.predict('number_plate.jpg')
    r= (result[0]["rec_texts"])
    return str(r[0])
