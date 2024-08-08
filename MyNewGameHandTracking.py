import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # Use 0 if you only have one camera
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

detector = htm.handDetector()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture image")
        break

    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Uncomment the following line if you want to display the FPS on the image
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
    #             (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Added condition to exit on pressing 'q'
        break

cap.release()
cv2.destroyAllWindows()
