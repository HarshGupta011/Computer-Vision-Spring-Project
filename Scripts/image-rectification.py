import cv2
import numpy as np

# Function to mouse callback
def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        if len(points) == 4:
            # Warp the image
            width, height = 200, 300
            src_pts = np.float32(points)
            dst_pts = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
            M = cv2.getPerspectiveTransform(src_pts, dst_pts)
            warped = cv2.warpPerspective(img, M, (width, height))

            # Show the cropped image
            cv2.imshow('Cropped Image', warped)
            cv2.imwrite('cropped_image.jpg', warped)
            # cv2.imwrite('results/Q2

# Load the image
img = cv2.imread('images/IMG_6625.jpeg')
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)
points = []

while True:
    # Show the image and wait for user input
    cv2.imshow('Image', img)
    key = cv2.waitKey(1) & 0xFF

    # Quit if the user presses 'q'
    if key == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
