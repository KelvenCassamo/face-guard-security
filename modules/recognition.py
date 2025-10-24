import threading

import cv2
import numpy as np
import face_recognition
from database import load_database
from playsound import playsound


alarm_playing = False

def play_alarm():
    global alarm_playing
    if not alarm_playing:
        alarm_playing = True
        threading.Thread(target=play_alarm_sound).start()

def play_alarm_sound():
    try:
        playsound('sounds/intruso.wav')
    finally:

        global alarm_playing
        alarm_playing = False


def recognize_face():
    
    video_capture = cv2.VideoCapture(0)
    print("A capturar imagem para reconhecimento... Olhe para a câmera e pressione 'q' para capturar.")

    while True:
        ret, frame = video_capture.read()
        cv2.imshow("Video", frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    
    face_encodings = face_recognition.face_encodings(frame)

    if len(face_encodings) == 0:
        print("Nenhum rosto detectado. Tente novamente.")
        return

    
    face_encoding = face_encodings[0]

    
    database = load_database()

    
    known_names = list(database.keys())
    known_encodings = [database[name]["encoding"] for name in known_names]

    
    matches = face_recognition.compare_faces(known_encodings, face_encoding)
    face_distances = face_recognition.face_distance(known_encodings, face_encoding)

    if True in matches:
        best_match_index = np.argmin(face_distances)
        name = known_names[best_match_index]
        age = database[name]["age"]
        print(f"Rosto reconhecido: {name}")
    else:
        print("Rosto não reconhecido.")





def recognize_faces_in_real_time():
    
    video_capture = cv2.VideoCapture(0)

    
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 850)  
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  
    video_capture.set(cv2.CAP_PROP_FPS, 30)  
    print("Reconhecimento de rostos em tempo real. Pressione 'q' para sair.")

    
    database = load_database()
    known_names = list(database.keys())
    known_encodings = [database[name]["encoding"] for name in known_names]
    frame_skip = 2  
    frame_count = 0
    while True:
        ret, frame = video_capture.read()

        
        frame_count += 1
        if frame_count % frame_skip != 0:
            continue
            pass
        
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)

            
            if True in matches:
                best_match_index = np.argmin(face_distances)
                name = known_names[best_match_index]
                age = database[name]["age"]

                
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, f"{name}", (left, top - 10),
                            cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

            else:
                
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, "Desconhecido", (left, top - 10),
                            cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

        
        cv2.imshow("Video", frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()



def recognize_all_faces():
    
    video_capture = cv2.VideoCapture(0)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)  
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 860)  
    print("A capturar imagem para reconhecimento de múltiplos rostos... Olhe para a câmera e pressione 'q' para capturar.")

    while True:
        ret, frame = video_capture.read()
        cv2.imshow("Video", frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    
    face_encodings = face_recognition.face_encodings(frame)

    if len(face_encodings) == 0:
        print("Nenhum rosto detectado. Tente novamente.")
        return

    
    database = load_database()

    
    known_names = list(database.keys())
    known_encodings = [database[name]["encoding"] for name in known_names]

    
    recognized = False
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)

        if True in matches:
            best_match_index = np.argmin(face_distances)
            name = known_names[best_match_index]
            age = database[name]["age"]
            print(f"Rosto reconhecido: {name}")
            recognized = True

    if not recognized:
        print("Nenhum rosto reconhecido.")



def recognize_theft_faces_in_real_time():
    
    video_capture = cv2.VideoCapture(0)

    
    #video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  
    #video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 850)  
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  
    video_capture.set(cv2.CAP_PROP_FPS, 30)  
    print("Reconhecimento de rostos em tempo real. Pressione 'q' para sair.")

    
    database = load_database()
    known_names = list(database.keys())
    known_encodings = [database[name]["encoding"] for name in known_names]

    frame_skip = 2
    frame_count = 0

    while True:
        ret, frame = video_capture.read()


        
        frame_count += 1
        if frame_count % frame_skip != 0:
            #continue
            pass
        
        face_locations = face_recognition.face_locations(frame, number_of_times_to_upsample=1)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)

            
            if True in matches:
                best_match_index = np.argmin(face_distances)
                name = known_names[best_match_index]
                age = database[name]["age"]

                
                if name.lower() == 'ataide':
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, f"{name} (INTRUSO)", (left, top - 10),
                                cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
                    print("Ataide detectado! A tocar alarme...")
                    play_alarm()
                else:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, f"{name}", (left, top - 10),
                                cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

            else:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, "Desconhecido", (left, top - 10),
                            cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
                print("Rosto desconhecido! A tocar alarme...")
                #play_alarm()

        
        cv2.imshow("Video", frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()