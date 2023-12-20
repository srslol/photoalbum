import cv2
import ctypes

# Get the window size and calculate the center
user32 = ctypes.windll.user32
win_x, win_y = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
win_cnt_x, win_cnt_y = [user32.GetSystemMetrics(0)/2, user32.GetSystemMetrics(1)/2] 

# load image
imgwindow = 'show my image'
image = cv2.imread('./images/20amp.png')

# Get the image size information
off_height, off_width = image.shape[:2]
off_height /= 2
off_width /= 2

# Show image and move it to center location
image = cv2.resize(image,(win_x, win_y))
cv2.imshow(imgwindow,image)

cv2.moveWindow(imgwindow,0,0)
cv2.waitKey(0)
cv2.destroyAllWindows()