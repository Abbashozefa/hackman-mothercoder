import cv2
import dlib
import pyttsx3
from scipy.spatial import distance



def Detect_Eye(eye):

        poi_A = distance.euclidean(eye[1], eye[5])
        poi_B = distance.euclidean(eye[2], eye[4])
        poi_C = distance.euclidean(eye[0], eye[3])
        aspect_ratio_Eye = (poi_A+poi_B)/(2*poi_C)
        return aspect_ratio_Eye


def yawnDetect(yawn):
        poi_A = distance.euclidean(yawn[2], yawn[10])
        poi_B = distance.euclidean(yawn[4], yawn[8])
        poi_C = distance.euclidean(yawn[0], yawn[6])
        aspect_ratio_yawn = (poi_A+poi_B)/(2*poi_C)
        return aspect_ratio_yawn

        