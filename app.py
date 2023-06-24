from flask import Flask,request,render_template,Response,redirect
import cv2
import dlib
import pickle
# from config import Config
# import time
# import numpy as np
# from playsound import playsound
# import os
import winsound
frequency = 3000  # Set Frequency To 2500 Hertz
duration = 150 # Set Duration To 1000 ms == 1 second
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import drowsymain as dm
import firebase_admin
from firebase_admin import credentials,storage
# app.config.from_object(Config)

cred = credentials.Certificate("wakey-wakey-a8b54-c78384195c1f.json")
firebase_admin.initialize_app(cred,{'storageBucket':'wakey-wakey-a8b54.appspot.com'})

from variables import Var
# engine = pyttsx3.init()
import plivo
import beepy

face_detector = dlib.get_frontal_face_detector()
 
# PUT THE LOCATION OF .DAT FILE (FILE
# FOR PREDECTING THE LANDMARKS ON FACE )
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

import pyrebase
# def yawn_countreturn():
#     return yawn_count
#Add your own details
config = {
  "apiKey": "PASTE_HERE",
  "authDomain": "PASTE_HERE",
  "databaseURL": "https://wakey-wakey-a8b54-default-rtdb.firebaseio.com/",
  "storageBucket": "PASTE_HERE"
}



#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
# from firebase import firebase
#Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}
# firebase1 = firebase.FirebaseApplication('', None)

model=pickle.load(open('alertmodel.pkl','rb'))
     



app=Flask(__name__)


def gen_frames():
    global cap
    cap = cv2.VideoCapture(0)
    
    
    Var.t=[]
    
    Var.yawn_count=0
    
    # MAIN LOOP IT WILL RUN ALL THE UNLESS AND
    # UNTIL THE PROGRAM IS BEING KILLED BY THE
    # USER
    while True:
        
        
        null, frame = cap.read()
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
        faces = face_detector(gray_scale)
     
        for face in faces:
            face_landmarks = dlib_facelandmark(gray_scale, face)
            leftEye = []
            rightEye = []
            yawn=[]
     
            # THESE ARE THE POINTS ALLOCATION FOR THE
            # LEFT EYES IN .DAT FILE THAT ARE FROM 42 TO 47
            for n in range(42, 48):
                x1 = face_landmarks.part(n).x
                y1 = face_landmarks.part(n).y
                rightEye.append((x1, y1))
                next_point = n+1
                if n == 47:
                    next_point = 42
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
     
            # THESE ARE THE POINTS ALLOCATION FOR THE
            # RIGHT EYES IN .DAT FILE THAT ARE FROM 36 TO 41
            for n in range(36, 42):
                x1 = face_landmarks.part(n).x
                y1 = face_landmarks.part(n).y
                leftEye.append((x1, y1))
                next_point = n+1
                if n == 41:
                    next_point = 36
                x2 = face_landmarks.part(next_point).x
                y2 = face_landmarks.part(next_point).y
                cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 1)
            right_Eye = dm.Detect_Eye(rightEye)
            left_Eye = dm.Detect_Eye(leftEye)
            Eye_Rat = (left_Eye+right_Eye)/2
     
            
            Eye_Rat = round(Eye_Rat, 2)
            for n in range(48,61):
                x1=face_landmarks.part(n).x
                y1=face_landmarks.part(n).y
                yawn.append((x1,y1))
                next_point=n+1
                if n==60:
                    next_point=48
                x2=face_landmarks.part(next_point).x
                y2=face_landmarks.part(next_point).y
                cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 1)
            yawn_data = dm.yawnDetect(yawn)
            yawn_data = round(yawn_data, 2)
            # print(yawn_data)
            print(Var.yawn_count)
                     
            
            if Eye_Rat < 0.25:
                # print(sum(t))
                # start=time.time()
                cv2.putText(frame, "DROWSINESS", (50, 100),
                            cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
                # cv2.putText(frame, "WAKE UP", (50, 450),
                #             cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 212), 3)
                # beepy.beep(sound="ping")
                winsound.Beep(frequency, duration)
                # CALLING THE AUDIO FUNCTION OF TEXT TO AUDIO
                # FOR ALERTING THE PERSON
                # end=time.time()
                # wave_obj = simpleaudio.WaveObject.from_wave_file("alarm.mp3")
                # play_obj = wave_obj.play()
                # play_obj.wait_done()
                Var.eye_drow_sec.append(0.50)
                

            Var.eye_drow_sec.append(0)   
            if yawn_data > 0.5:
                
                Var.yawn_count=Var.yawn_count+1
                Var.yawn_sec.append(0.50)
                cv2.putText(frame, "Yawning", (100, 450),
                            cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
                
                # engine.say("Alert!")
            
                # engine.startLoop(False)
                # engine.endLoop()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')       
     
        # cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
    #     key = cv2.waitKey(9)
    #     if key == 20:
    #         break
    # cap.release()
    # cv2.destroyAllWindows()


# def gen_frames1():
#     global cap
#     # cap = cv2.VideoCapture(0)
#     global t
#     t=[]
#     global yawn_count
#     yawn_count=0
#     # MAIN LOOP IT WILL RUN ALL THE UNLESS AND
#     # UNTIL THE PROGRAM IS BEING KILLED BY THE
#     # USER
#     while True:
        
        
#         null, frame = cap.read()
#         gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
#         faces = face_detector(gray_scale)
     
#         for face in faces:
#             face_landmarks = dlib_facelandmark(gray_scale, face)
#             leftEye = []
#             rightEye = []
#             yawn=[]
     
#             # THESE ARE THE POINTS ALLOCATION FOR THE
#             # LEFT EYES IN .DAT FILE THAT ARE FROM 42 TO 47
#             for n in range(42, 48):
#                 x1 = face_landmarks.part(n).x
#                 y1 = face_landmarks.part(n).y
#                 rightEye.append((x1, y1))
#                 next_point = n+1
#                 if n == 47:
#                     next_point = 42
#                 x2 = face_landmarks.part(next_point).x
#                 y2 = face_landmarks.part(next_point).y
#                 cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
     
#             # THESE ARE THE POINTS ALLOCATION FOR THE
#             # RIGHT EYES IN .DAT FILE THAT ARE FROM 36 TO 41
#             for n in range(36, 42):
#                 x1 = face_landmarks.part(n).x
#                 y1 = face_landmarks.part(n).y
#                 leftEye.append((x1, y1))
#                 next_point = n+1
#                 if n == 41:
#                     next_point = 36
#                 x2 = face_landmarks.part(next_point).x
#                 y2 = face_landmarks.part(next_point).y
#                 cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 1)
#             right_Eye = dm.Detect_Eye(rightEye)
#             left_Eye = dm.Detect_Eye(leftEye)
#             Eye_Rat = (left_Eye+right_Eye)/2
     
            
#             Eye_Rat = round(Eye_Rat, 2)
#             for n in range(48,61):
#                 x1=face_landmarks.part(n).x
#                 y1=face_landmarks.part(n).y
#                 yawn.append((x1,y1))
#                 next_point=n+1
#                 if n==60:
#                     next_point=48
#                 x2=face_landmarks.part(next_point).x
#                 y2=face_landmarks.part(next_point).y
#                 cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 1)
#             yawn_data = dm.yawnDetect(yawn)
#             yawn_data = round(yawn_data, 2)
#             # print(yawn_data)
#             print(yawn_count)
                     
            
#             if Eye_Rat < 0.25:
#                 print(sum(t))
#                 # start=time.time()
#                 cv2.putText(frame, "DROWSINESS DETECTED", (50, 100),
#                             cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
#                 # cv2.putText(frame, "WAKE UP", (50, 450),
#                 #             cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 212), 3)
                
#                 winsound.Beep(frequency, duration)
#                 # CALLING THE AUDIO FUNCTION OF TEXT TO AUDIO
#                 # FOR ALERTING THE PERSON
#                 # end=time.time()
#                 t.append(0.50)
#                 t.append(0.50)

#             t.append(0)   
#             if yawn_data > 0.5:
                
#                 yawn_count=yawn_count+1
#                 cv2.putText(frame, "Yawning", (100, 450),
#                             cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
                
#                 # engine.say("Alert!")
            
#                 # engine.startLoop(False)
#                 # engine.endLoop()
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')       
     
#         # cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
#     #     key = cv2.waitKey(9)
#     #     if key == 20:
#     #         break
#     # cap.release()
#     # cv2.destroyAllWindows()


    



@app.route('/')
def home():
    username= request.args.get('user')
    print(username)
    # global t
    # global yawn_count
    deccelerate=sum(Var.eye_drow_sec)+Var.yawn_count+sum(Var.yawn_sec)
    print(deccelerate)
    userdetails={'dec':deccelerate}
    print(sum(Var.eye_drow_sec))
    alert=model.predict([[sum(Var.eye_drow_sec),Var.yawn_count,sum(Var.yawn_sec)]])
    print("alert is",alert[0])
    if alert[0]==1:
        if deccelerate>45:
            userdetails['low']='0'
            userdetails['high']='5'
            userdetails['color']='red'
            json_data = {'alert':'true'}   
            # name = "abbas"
            # address = "bangalore"
            # new_data = {"name": name, "address": address}
            # firebase1.post("/contact", new_data)
            u = db.child("contact").child(username).update(json_data)
            print("done")
            dr=Var.eye_drow_sec.count(0.5)
            ndr=Var.eye_drow_sec.count(0)
            file_path = str(username)+".png"
            plt.pie([dr,ndr],labels=['Drowsiness','Awake'],colors=['red','green'])
            plt.legend()
    
            plt.savefig(file_path)
            # auth_id = 'MANJKWMTQ3YZLJOWI3MJ'
            # auth_token = 'ZTk0MzYwNTdkYTJkNTI2MzZlNjRlMTAyNmM0NjRj'
            # phlo_id = '71b3cd61-3d32-48e2-838f-497a4d06706e' # https://console.plivo.com/phlo/list/
            # phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
            # phlo = phlo_client.phlo.get(phlo_id)
            # phlo.run() 
            
            bucket = storage.bucket() # storage bucket
            blob = bucket.blob(file_path)
            blob.upload_from_filename(file_path)
        elif deccelerate>30:
            userdetails['low']='5'
            userdetails['high']='10'
            userdetails['color']='yellow'
            json_data = {'alert':'true'}   
            # name = "abbas"
            # address = "bangalore"
            # new_data = {"name": name, "address": address}
            # firebase1.post("/contact", new_data)
            u = db.child("contact").child(username).update(json_data)
            print("done")
            dr=Var.eye_drow_sec.count(0.5)
            ndr=Var.eye_drow_sec.count(0)
            file_path = str(username)+".png"
            plt.pie([dr,ndr],labels=['Drowsiness','Awake'],colors=['red','green'])
            plt.legend()
    
            plt.savefig(file_path)
            # auth_id = 'MANJKWMTQ3YZLJOWI3MJ'
            # auth_token = 'ZTk0MzYwNTdkYTJkNTI2MzZlNjRlMTAyNmM0NjRj'
            # phlo_id = '71b3cd61-3d32-48e2-838f-497a4d06706e' # https://console.plivo.com/phlo/list/
            # phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
            # phlo = phlo_client.phlo.get(phlo_id)
            # phlo.run() 
            
            bucket = storage.bucket() # storage bucket
            blob = bucket.blob(file_path)
            blob.upload_from_filename(file_path)
        elif deccelerate>20:
            userdetails['low']='10'
            userdetails['high']='12'
            userdetails['color']='blue'
            json_data = {'alert':'true'}   
            # name = "abbas"
            # address = "bangalore"
            # new_data = {"name": name, "address": address}
            # firebase1.post("/contact", new_data)
            u = db.child("contact").child(username).update(json_data)
            print("done")
            dr=Var.eye_drow_sec.count(0.5)
            ndr=Var.eye_drow_sec.count(0)
            file_path = str(username)+".png"
            plt.pie([dr,ndr],labels=['Drowsiness','Awake'],colors=['red','green'])
            plt.legend()
    
            plt.savefig(file_path)
            # auth_id = 'MANJKWMTQ3YZLJOWI3MJ'
            # auth_token = 'ZTk0MzYwNTdkYTJkNTI2MzZlNjRlMTAyNmM0NjRj'
            # phlo_id = '71b3cd61-3d32-48e2-838f-497a4d06706e' # https://console.plivo.com/phlo/list/
            # phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
            # phlo = phlo_client.phlo.get(phlo_id)
            # phlo.run() 
            
            bucket = storage.bucket() # storage bucket
            blob = bucket.blob(file_path)
            blob.upload_from_filename(file_path)
        else:
            userdetails['low']='12'
            userdetails['high']='18'
            userdetails['color']='green'
            json_data = {'alert':'true'}   
            # name = "abbas"
            # address = "bangalore"
            # new_data = {"name": name, "address": address}
            # firebase1.post("/contact", new_data)
            u = db.child("contact").child(username).update(json_data)
            print("done")
            dr=Var.eye_drow_sec.count(0.5)
            ndr=Var.eye_drow_sec.count(0)
            file_path = str(username)+".png"
            plt.pie([dr,ndr],labels=['Drowsiness','Awake'],colors=['red','green'])
            plt.legend()
    
            plt.savefig(file_path)
            # auth_id = 'MANJKWMTQ3YZLJOWI3MJ'
            # auth_token = 'ZTk0MzYwNTdkYTJkNTI2MzZlNjRlMTAyNmM0NjRj'
            # phlo_id = '71b3cd61-3d32-48e2-838f-497a4d06706e' # https://console.plivo.com/phlo/list/
            # phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
            # phlo = phlo_client.phlo.get(phlo_id)
            # phlo.run() 
            
            bucket = storage.bucket() # storage bucket
            blob = bucket.blob(file_path)
            blob.upload_from_filename(file_path)
    else:
        userdetails['low']='Average'
        userdetails['high']='Speed'
        userdetails['color']='green'
        json_data = {'alert':'false'}    
        u = db.child("contact").child(username).update(json_data)
        print("done")
        dr=Var.eye_drow_sec.count(0.5)
        ndr=Var.eye_drow_sec.count(0)
        file_path = str(username)+".png"
        plt.pie([dr,ndr],labels=['Drowsiness','Awake'],colors=['red','green'])
        plt.legend()
        plt.savefig(file_path)
        bucket = storage.bucket() # storage bucket
        blob = bucket.blob(file_path)
        blob.upload_from_filename(file_path)
    
             
             
        
    
    
    return render_template('temp.html',userdetails=userdetails)

@app.route('/start',methods=['POST'])
def start():
    return render_template('index.html')

@app.route('/stop',methods=['POST','GET'])
def stop():
    # username= request.args.get('user')
    # if sum(t)>10 and yawn_count>2:
    #     auth_id = 'MANJKWMTQ3YZLJOWI3MJ'
    #     auth_token = 'ZTk0MzYwNTdkYTJkNTI2MzZlNjRlMTAyNmM0NjRj'
    #     phlo_id = '71b3cd61-3d32-48e2-838f-497a4d06706e' # https://console.plivo.com/phlo/list/
    #     phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
    #     phlo = phlo_client.phlo.get(phlo_id)
    #     phlo.run()
    # dr=Var.t.count(0.5)
    # ndr=Var.t.count(0)
    # plt.pie([dr,ndr],labels=['Drowsiness','Awake'],colors=['red','blue'])
    # plt.savefig('visual.png')
    # print("done")
    
    # if cap.isOpened():        
    #     cap.release()
        
    return render_template('stop.html')





@app.route('/video_feed')
def video_feed():
    
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

#Login
# @app.route("/")
# def login():
#     return render_template("login.html")




# @app.route('/video_feed1')
# def video_feed1():
#     return Response(gen_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')




# @app.route("/welcome")
# def welcome():
#     if person["is_logged_in"] == True:
#         return render_template("welcome.html", email = person["email"], name = person["name"])
#     else:
#         return redirect(url_for('login'))

# #If someone clicks on login, they are redirected to /result
# @app.route("/result", methods = ["POST", "GET"])
# def result():
#     if request.method == "POST":        #Only if data has been posted
#         result = request.form           #Get the data
#         email = result["email"]
#         password = result["pass"]
#         try:
#             #Try signing in the user with the given information
#             user = auth.sign_in_with_email_and_password(email, password)
#             #Insert the user data in the global person
#             global person
#             person["is_logged_in"] = True
#             person["email"] = user["email"]
#             person["uid"] = user["localId"]
#             #Get the name of the user
#             data = db.child("users").get()
#             person["name"] = data.val()[person["uid"]]["name"]
#             #Redirect to welcome page
#             return redirect(url_for('welcome'))
#         except:
#             #If there is any error, redirect back to login
#             return redirect(url_for('login'))
#     else:
#         if person["is_logged_in"] == True:
#             return redirect(url_for('welcome'))
#         else:
#             return redirect(url_for('login'))






if __name__ == '__main__':
    
    app.run(port=5000,debug=True)