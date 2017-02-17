# CraterModeling_complete
Toolbox to calculate multiple crater  profiles

#Instructions of use

First, you need to pass your IMG file throught the Python script that transforms IMG to a matlab readable format.
 Be sure to have GDAL installed 
 
 This is a relevant thread in stackoverflow (http://gis.stackexchange.com/questions/2276/installing-gdal-with-python-on-windows)
 
After you run the Python file, you need to run the matlab file : main_multiple_craters.m

You can click multiple craters in the image, just be sure that you click 3 points per crater.
The default rate of angle increases is 0.1 radian, but this can be adjusted in line 35 (variable angle_step)

