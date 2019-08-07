import cv2
import numpy as np
from sklearn import svm
import os, shutil
import sys
# from PIL import Image



files1=os.listdir("bharatanatyam\\1")
files2=os.listdir("bharatanatyam\\2")
files3=os.listdir("bharatanatyam\\3")
files4=os.listdir("bharatanatyam\\4")
files5=os.listdir("bharatanatyam\\5")
files6=os.listdir("bharatanatyam\\6")
files7=os.listdir("bharatanatyam\\7")
files8=os.listdir("odissi\\1")
files9=os.listdir("odissi\\2")
files10=os.listdir("odissi\\3")
files11=os.listdir("odissi\\4")
files12=os.listdir("kathak\\1")
files13=os.listdir("kathak\\2")
files14=os.listdir("kathak\\3")
files15=os.listdir("kathak\\4")
files16=os.listdir("kathak\\5")
files17=os.listdir("mohiniyattam")
files18=os.listdir("kuchipudi")
files19=os.listdir("sattriya")
files20=os.listdir("manipuri")
files21=os.listdir("kathakali")

#print len(files)
x = np.zeros((len(files1) + len(files2)+ len(files4)+ len(files5)+ len(files6)+ len(files8)+
              len(files9)+ len(files10) +len(files11) + len(files12) + len(files13)+ len(files14)+ len(files15)+ len(files16)+len(files17)
              +len(files18) +len(files19)+len(files20)
            +len(files21) ,7))
            #   ,7))
count=0
labels=[]

#*****************************************************************
PATH="bharatanatyam/1/"

for idx,filename in enumerate(files1):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        # print(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # print(image)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        # print(feature)    #flatten() gives the shape featured vector 
        features = -np.sign(feature) * np.log10(np.abs(feature))
        # print(features)
        x[count]=features
        labels.append(1)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="bharatanatyam/2/"

for idx,filename in enumerate(files2):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(2)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="bharatanatyam/3/"

for idx,filename in enumerate(files3):
   if filename!="Thumbs.db":
       infile=PATH+filename
       #outfile="1/"+filename
       image = cv2.imread(infile)
       image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       feature = cv2.HuMoments(cv2.moments(image)).flatten()
       features = -np.sign(feature) * np.log10(np.abs(feature))
       x[count]=features
       labels.append(3)
       count=count+1
       #print features

#*****************************************************************
#*****************************************************************
PATH="bharatanatyam/4/"

for idx,filename in enumerate(files4):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(4)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="bharatanatyam/5/"

for idx,filename in enumerate(files5):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(5)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="bharatanatyam/6/"

for idx,filename in enumerate(files6):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(6)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="bharatanatyam/7/"

for idx,filename in enumerate(files7):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(7)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="odissi/1/"

for idx,filename in enumerate(files8):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(8)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="odissi/2/"

for idx,filename in enumerate(files9):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(9)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="odissi/3/"

for idx,filename in enumerate(files10):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(10)
        count=count+1
        #print features

#*****************************************************************
#*****************************************************************
PATH="odissi/4/"

for idx,filename in enumerate(files11):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(11)
        count=count+1
        #print features


#*****************************************************************

#*****************************************************************
PATH="kathak/1/"

for idx,filename in enumerate(files12):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(12)
        count=count+1
        #print features


#*****************************************************************
#*****************************************************************
PATH="kathak/2/"

for idx,filename in enumerate(files13):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(13)
        count=count+1
        #print features


#*****************************************************************
#*****************************************************************
PATH="kathak/3/"

for idx,filename in enumerate(files14):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(14)
        count=count+1
        #print features


#*****************************************************************
#*****************************************************************
PATH="kathak/4/"

for idx,filename in enumerate(files15):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(15)
        count=count+1
        #print features


#*****************************************************************
#*****************************************************************
PATH="kathak/5/"

for idx,filename in enumerate(files16):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(16)
        count=count+1
        #print features

PATH="mohiniyattam/"

for idx,filename in enumerate(files17):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(17)
        count=count+1
        #print features

# *****************************************************************      

PATH="kuchipudi/"

for idx,filename in enumerate(files18):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(18)
        count=count+1
        #print features

#*****************************************************************      

PATH="sattriya/"

for idx,filename in enumerate(files19):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(19)
        count=count+1
        #print features

#*****************************************************************      

PATH="manipuri/"

for idx,filename in enumerate(files20):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(20)
        count=count+1
        #print features

 # *****************************************************************      

PATH="kathakali/"

for idx,filename in enumerate(files21):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features
        labels.append(21)
        count=count+1
        #print features

# *****************************************************************        


for i in range (0,len(x)-len(labels)):
	labels.append(11)

#***********************************traning*********************
#x = -np.sign(x) * np.log10(np.abs(x))	
#print repr(x)
clf = svm.SVC(kernel='linear',C = 1.0)
#clf = svm.SVC( kernel='rbf',C = 1.0,gamma = 'auto')
clf.fit(x,labels)

# print ("Traning done")



# testing for videos
import cv2
vidcap = cv2.VideoCapture('dip/manipuri.mp4')
success,image = vidcap.read()
count = 0
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
  #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
#   print('Read a new frame: ', success)
  if(success==True and count>10):
    cv2.imwrite("video_test/frame%d.jpg" % count, image)     # save frame as JPEG file  
  count += 1
  if(count==300):
      break


test=os.listdir("video_test\\")
PATH="video_test/"
freq=[0,0,0,0,0,0,0,0]
names=["Bharatanatyam","Odissi","Kathak", "Mohiniyattam","Kuchipudi","Sattriya","Manipuri","Kathakali"]
for idx,filename in enumerate(test):
    if filename!="Thumbs.db":
        infile=PATH+filename
        #outfile="1/"+filename
        image = cv2.imread(infile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        number=clf.predict([features])
        # print(clf.predict([features]))
        
        if(number>=1 and number<=7):
            dance = "Bharatanatyam"
            freq[0]+=1
        elif(number>=8 and number<=11):
            dance = "Odissi"
            freq[1]+=1
        elif(number>=12 and number<=16):
            dance = "Kathak"
            freq[2]+=1
        elif(number==17):
            dance = "Mohiniyattam"
            freq[3]+=1
        elif(number==18):
            dance = "Kuchipudi"
            freq[4]+=1
        elif(number==19):
            dance = "Sattriya"
            freq[5]+=1
        elif(number==20):
            dance = "Manipuri"
            freq[6]+=1
        elif(number==21):
            dance = "Kathakali"
            freq[7]+=1
        # print (filename,dance)
        # print (filename,clf.predict(features))
pos=freq.index(max(freq))
# print(freq)
print(names[pos])

# deleting files after execution
folder = 'video_test/'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

