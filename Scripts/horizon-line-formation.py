import cv2
import numpy as np
# Define global variables to store clicked points
red_points = []
blue_points = []

def compute_intersection(line1, line2):
    """
    Computes the intersection point of two lines given in the form of [(x1, y1), (x2, y2)].
    Returns None if the lines are parallel.
    """
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denom == 0:
        # Lines are parallel
        return None
    else:
        x = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
        y = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
        return (int(x), int(y))

# Mouse event callback function to handle clicks
def mouse_callback(event, x, y, flags, param):
    global red_points, blue_points
    
    if event == cv2.EVENT_LBUTTONUP:
        # For red vanishing lines
        if len(red_points) < 4:
            red_points.append((x, y))
        # For blue vanishing lines
        elif len(blue_points) < 4:
            blue_points.append((x, y))

# Load the image and display it
img = cv2.imread('images/IMG_6566.jpg')
cv2.namedWindow("Image")
cv2.imshow("Image", img)

# Register the mouse callback function
cv2.setMouseCallback("Image", mouse_callback)

# Keep looping until we have all points
while True:
    # Draw the red lines
    if len(red_points) == 2:
        cv2.line(img, red_points[0], red_points[1], (0, 0, 255), 2)
    if len(red_points) == 4:
        cv2.line(img, red_points[2], red_points[3], (0, 0, 255), 2)
        
    # Draw the blue lines
    if len(blue_points) == 2:
        cv2.line(img, blue_points[0], blue_points[1], (255, 0, 0), 2)
    if len(blue_points) == 4:
        cv2.line(img, blue_points[2], blue_points[3], (255, 0, 0), 2)
        
    # Show the image with lines
    cv2.imshow("Image", img)
    
    # Check if we have all points
    if len(red_points) == 4 and len(blue_points) == 4:
        break
        
    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Find the intersection points
red_intersect = compute_intersection(red_points[:2], red_points[2:])
blue_intersect = compute_intersection(blue_points[:2], blue_points[2:])

# Connecting the two red lines and the two blue lines
cv2.line(img, red_points[2], red_intersect, (0, 0, 255), 2)
cv2.line(img, red_points[1], red_intersect, (0, 0, 255), 2)
cv2.line(img, blue_points[2], blue_intersect, (255, 0, 0), 2)
cv2.line(img, blue_points[1], blue_intersect, (255, 0, 0), 2)

# Draw the green horizon line
cv2.line(img, (int(red_intersect[0]), int(red_intersect[1])),
         (int(blue_intersect[0]), int(blue_intersect[1])),
         (0, 255, 0), 2)

# Show the final image with horizon line
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

