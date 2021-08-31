
# import the required modules
import os
try:
    import filetype
except:
    os.system('pip install filetype')
    import filetype
try:
    import cv2
except:
    os.system('pip install opencv-python')
    import cv2
try:
    from matplotlib import pyplot as plt, transforms
except:
    os.system('pip install matplotlib')
    from matplotlib import pyplot as plt, transforms
try:
    import easygui
except:
    os.system('pip install easygui')
    import easygui

def openfile():
    path = easygui.fileopenbox()
    if filetype.is_image(path):
        print('[+]Valid File')
        return path
    else:
        print('[-]Invalid file')
        exit()
# Read the image
path=openfile()
img = cv2.imread(path, 0)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# Apply median blur
#img = cv2.Canny(img,100,200)

# img = cv2.medianBlur(edges, 5)

# Apply MEAN thresholding to get refined edges
image = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Convert the image into a compatible size
# We will use 60 pixels wide image so that text
# fits in the console

# Preserve the ratio
ratio = len(image) / len(image[0])
# Assign new width and calculate new height
new_width = 60
new_height = int(ratio * new_width)
# Resize the image
image = cv2.resize(image, (new_height, new_width))

# Iterate over the array and print the dark pixels
# or we can use any other symbol too.
count=0
plt.figure(figsize=(10, 10))
plt.axis('off')
x,y=image.shape
for i in range(len(image)):
    for j in range(len(image[0])):
        if image[i, j] < 10:
            plt.plot(i, j, marker='.', color='black')
            count=count+1
        else:
            pass
plt.savefig("sample.jpg", orientation='landscape')
listofNo=list(range(0,count))
for k in range(len(image)):
    for m in range(len(image[0])):
        if image[k,m]<10:
            plt.annotate(listofNo[k], (k, m))

plt.savefig("sample1.jpg", orientation='landscape')