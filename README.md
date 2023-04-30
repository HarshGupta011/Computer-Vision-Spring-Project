# Computer-Vision-Spring-Project CSCI 5722
Solution for 4 tasks: Image stitching, Changing the view of an image, Rectification of an image, and, finding the Horizon Line in an Image
## Part 1: Image Stitching
Objectives:

In this experiment, you were asked to find homography between two images to generate a panorama image. As shown in the examples, you should take pictures of an object (i.g a building) by rotating your camera. 
<img width="581" alt="Screenshot 2023-04-29 at 6 57 50 PM" src="https://user-images.githubusercontent.com/31663796/235330412-8cbbf977-9ec3-44a0-9842-b3c2e5a60b52.png">
Fig 1. Image Stitching

First, you should manually select the corresponding points in two images. It is important to ensure that the selected points are in the same order.
<img width="437" alt="Screenshot 2023-04-29 at 7 02 54 PM" src="https://user-images.githubusercontent.com/31663796/235330566-821395c5-b330-42ae-9c8e-332a0b24a477.png">
Four points are selected in two images above.

<img width="442" alt="Screenshot 2023-04-29 at 7 03 17 PM" src="https://user-images.githubusercontent.com/31663796/235330570-cf0ce49e-627a-473b-8e5d-52f83b3a615f.png">
The result of stitching.

## Part 2: Changing the view
Objectives:
In this experiment, you need to take pictures of an object from different viewpoints. Then, we will transition the viewpoint of the object from Picture 1 to Picture 2.

<img width="467" alt="Screenshot 2023-04-29 at 6 59 43 PM" src="https://user-images.githubusercontent.com/31663796/235330474-7f8fbcfb-84ef-4904-a368-4f4bc79fae82.png">
<img width="522" alt="Screenshot 2023-04-29 at 7 00 05 PM" src="https://user-images.githubusercontent.com/31663796/235330479-32e6be98-4d6a-474c-8cc2-b4fff92168ff.png">
Shows picture one transformed into the viewpoint of picture 2

## Part 3: Rectifying an image
Objectives:
In this experiment, you need to take pictures of an object from one view (left). Then, we will manually mark the four corners of an object. Then, you will warp a 4 sided polygon into a rectangle (right).
<img width="564" alt="Screenshot 2023-04-29 at 7 01 23 PM" src="https://user-images.githubusercontent.com/31663796/235330517-1eeec3bc-a221-478a-a59c-59e10caec51e.png">
The second picture is the front view of the first picture.

## Part 4: Horizon Line in an Image
Objectives
In this experiment, you need to take pictures of an object. Then, by finding vanishing points, you should be able to find the horizon line in that image as shown in the figure below.
<img width="622" alt="Screenshot 2023-04-29 at 7 02 26 PM" src="https://user-images.githubusercontent.com/31663796/235330544-1f0d8365-2e57-4798-b50e-edeb8bfea48a.png">

Red and blue lines are vanishing lines and the green line is the horizon line in this image.

You can select points manually. Then, by finding the intersection of lines in each plane, you can find the vanishing point. The horizon line can then be determined by drawing a line connecting the two vanishing points. 
