import cv2 as cv
import sys
import time

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        sys.exit("Non trovo lo stream")
    while True:
        ret, frame = cap.read() #ret mi dice se è andato tutto bene, mentre frame contiene l'immagine
        if not ret:
            print("errore")
            continue
        frame = cv.flip(frame, 1) #specchio l'immagine ---> con questo invece modifico i colori frame= ~frame
        imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("frame", frame)
        cv.imshow("Gray", imgGray)
        if cv.waitKey(1) == ord("q"):
            break
    cap.release()           #queste due righe le utilizziamo per fare pulizia
    cv.destroyAllWindows()  #con questa chiudo tutte le finestre