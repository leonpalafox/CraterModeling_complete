#Script to generate a Matlab compliant file from a DTM with extension IMG
#Created by Leon F. Palafox
#Last Update: February, 17th, 2017
from osgeo import gdal #gdal hast to be installed and is the python library to work with Georeference data
import scipy.io
img_file = 'C:\Users\leon\Documents\Data\DTMimages\DTEEC_041277_2115_040776_2115_A01.IMG' #put the path and filename here, be careful on file conventions in Mac or Windows
g = gdal.Open(img_file) #Open the file to work with it
b = g.GetRasterBand(1) #Get bands
a = b.ReadAsArray() #get image 
high_limit = a.max()
a[a==a.min()]=a.max()+1; #Take out those pesky black areas (and this is the new a.max())
low_limit = a.min()
mid_value = (high_limit-low_limit)/2+low_limit;
a[a==a.max()] = (high_limit-low_limit)/2+low_limit;
scipy.io.savemat('C:\Users\leon\Documents\Data/DTMimages/DTEEC_041277_2115_040776_2115_A01.mat', mdict={'a': a}) #Here is where we save the data to anayse it in Matlab