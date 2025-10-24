import cv2
import face_recognition
from database import load_database, save_database


def register_face(name, age):
    
    video_capture = cv2.VideoCapture(0)
    print("Capturando imagem... Olhe para a câmera e pressione 'q' para capturar.")

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

    
    database[name] = {
        "age": age,
        "encoding": face_encoding
    }

    save_database(database)
    print(f"Rosto de {name} registrado com sucesso!")



