import cv2
import time
import datetime
from twilio.rest import Client

cap = cv2.VideoCapture(0)

account_sid ="PACc582a9738f6f849cf1f1e409effc3615r"
auth_token ="ac83cc00539f0b504fc67b78669d37334d"

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(
                f"Videos\\{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
            img_path =f"{current_time}.png"
            cv2.imwrite(f"Images\\{img_path}", frame)
            cv2.imwrite(f"C:\\xampp\\htdocs\\Images\\{img_path}",frame)

            client = Client(account_sid, auth_token)

            to_whatsapp_number ="whatsapp:+919980797553"
            from_whatsapp_number = "whatsapp:+14155238886"

            message =client.messages.create(body="An Intruder found near your home",
            media_url=f"https://0e7d-117-248-88-21.in.ngrok.io/Images/{img_path}",
            from_=from_whatsapp_number,to=to_whatsapp_number)
            
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print('Stop Recording!')
               
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    for (x, y, width, height) in faces:
       cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()