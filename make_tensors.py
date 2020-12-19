from pytube import YouTube
from keras.models import load_model
import os
import shutil
import math
import datetime
# plots
import matplotlib.pyplot as plt
from utils import Videos
# image operation
import cv2

class Return_Tensor(object) :

  def give_me_tensor(self,link) :

    # this method will extract video from youtube and return the tensors
    # Expected input is of string class holding youtube link

    self.youtube_video_url = 'https://youtu.be/phm9S4g-jIo'
    yt_obj = YouTube(self.youtube_video_url)

    for stream in yt_obj.streams:
        print(stream)

    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    
    for mp4_filter in filters:
        print(mp4_filter)

    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    
    filters.get_highest_resolution()
    filters.get_lowest_resolution()

    video = filters.get_highest_resolution().download()
    print(video) 

    # initialising the class from the utils.py
    v = Videos()
    tensors = v.read_videos([video])

    #loading model
    model=load_model('final_model.h5')

    #making prediction
    pred=model.predict_classes(tensors)

    #loading our target dataset
    df=pd.read_csv('dataframe.csv')

    #checking relative activity name to the array
    activity_name=df[df['label_nums']==pred[0]]
    activity=activity_name.labels.unique()[0]

    return activity


