import cv2
img = cv2.imread(r'no_parking1.jpg')
num_plt = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
plt_detect = num_plt.detectMultiScale(img,1.2,4)
print(plt_detect)
for (x,y,w,h) in plt_detect:
    print(x,y)
    print(w,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,25),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
