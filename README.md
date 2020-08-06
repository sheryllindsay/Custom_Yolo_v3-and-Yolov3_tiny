# Yolo_v3 Yolov3_tiny
•	If your running yolov3 or yolov3 tiny, remember that their unique files are in their respective folders.
•	The common files are present outside the unique yolov3 folders.
•	For Yolov3, run Maxmoc_yolov3.ipynb and use its unique “obj.names”, “obj.data” and “yolov3_custom_cfg” files.
•	For Yolov3 tiny, run Maxmoc_yolov3_tiny.ipynb and use its unique “obj.names”, “obj.data” and “yolov3_tiny_custom_cfg” files.
  
 NOTE: We used google colab to train the model and loaded the dataset into our drive and connected out drive to our colab notebook.
  
1)	The detect video is an example showcasing how the end result is. We saved the detect video as a sample.
2)	In your google drive create a folder for yolov3:
  
a)	Save “obj.names”, “obj.data” and “yolov3_custom_cfg/yolov3_tiny_custom.cfg” into the file. 
b)	Load Maxmoc_yolov3 into your google colab and run the files. Do not run the 5th cell which is the pre-trained weights. It is time consuming.
c)	Connect your drive to colab.
d)	Make sure to change the path so that the paths in the code match where the necessary files are located. Especially when you unzip the datafiles, check where you zip file is located.
  
3)	Make sure not to run the next two commands as this will reset the cfg files.
# download cfg to google drive and change its name
!cp cfg/yolov3.cfg /mydrive/yolov3/yolov3_custom.cfg
  
4)	Run the remainder files and if the training stops in the middle, do not worry. You can start again from the cell that says “#if it stops”
5)	To test you have to change the cfg file. So, after testing revert back to training cfg.
6)	Make sure to set the paths right for the testing.
 NOTE: All the files necessary to train and test are present in the “Car_Truck_Bike_yolov3” folder. Please look for them carefully.
 Only yolov3 files have their weights converted to “tf” files to run in Object-Detection-API”. For yolov3-tiny, the weights have to be converted to “tf” files to run detections in Object-Detetction-API
