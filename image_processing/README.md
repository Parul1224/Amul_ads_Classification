The two files grid_removal.py and background_removal.py contains the code that carry out the basic image processing operations.
         


For running the above files check whether the below_mentioned modules are installed in your system or not.
1.PIL
2.numpy
3.cv2
4.python 2.7






1.The file "grid_removal.py" removes the grids from the image using cv2 library by applying canny edge detection and the technique of Hough Transform.
Command to run the file:
python grid_removal.py
Input the absolute path of your image.
Output will be stored in the folder "images" in the same directory labelled as "removed_grids.jpeg".









2.The file "background_removal.py" performs "background subtraction" and stores the output images in the folder "images" within the same directory "image_processing".
Command to execute the file
python background_detection.py
Specify the path of input image within the code itself.
The output will be saved in folder-"images" within the same directory.
