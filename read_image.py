import cv2
img=cv2.imread('huan.png',0)
(h,w)=img.shape
# def convert_image(img):
#     for i in range(h):
#         for j in range(w):
#             img[i][j]=255-img[i][j]
#     return img

f = open('huan.txt', 'w')
def convert_image(img):
    for i in range(h):
        for j in range(w):
            a=str(img[i][j])
            if img[i][j]>9:
                if img[i][j] > 99:
                    if img[i][j] > 230:
                        f.write('000')
                    else:
                        f.write(a)
                else:
                    f.write('0')
                    f.write(a)
            else:
                f.write('00')
                f.write(a)
        f.write('\n')
convert_image(img)
f.close()
cv2.waitKey(0)