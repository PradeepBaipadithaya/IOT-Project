# IOT-Project
IOT based security camera that sends intruder message in whatsapp

# Introduction
This is a project which is used to keep continuous monitor on your security camera system.

# Required software
1. Text Editor
2. Ngrok
3. Xampp
4. Python language

# Required module for python
1. cv2 (pip install cv2)
2. twilio (pip install twilio)

# Procedure
1. Clone this repository by using "git clone https://github.com/PradeepBaipadithaya/IOT-Project.git" in git bash.
2. Install the required package for python project.
3. Download ngrok software.
4. Download Xampp software and start "Apache" module.
5. Run ngrok software and type "ngrok http 80".
6. Copy paste url of ngrok to media_url of python code.
7. Have an account in Twilio and use those tokens.
8. Run the python code and you will get whatsapp message if any intruder gets caught in camera.
9. If you're using external web cam then make value of VideoCapture(0) as VideoCapture(1).

