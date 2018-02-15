import cv2

cap = cv2.VideoCapture(0)
i=0
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    i += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("C:\pylearning\ml&dl\\face_detect_v0\\test_img\\"+str(i)+'.jpg', frame)
        continue
cap.release()
cv2.destroyAllWindows()