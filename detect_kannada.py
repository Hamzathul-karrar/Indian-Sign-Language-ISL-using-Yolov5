import os
import subprocess

# Define the path to the YOLOv5 directory
yolov5_path = "C:\Indian-Sign-Language-ISL-using-Yolov5\"

# Change the current working directory to the YOLOv5 directory
os.chdir(yolov5_path)

command = "python detect.py --weights C:\Indian-Sign-Language-ISL-using-Yolov5\models\kannada.pt --img 640 --conf 0.25 --source 0 "

# Execute the command
subprocess.run(command, shell=True)
