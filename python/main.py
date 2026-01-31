from arduino.app_utils import App
from arduino.app_bricks.video_imageclassification import VideoImageClassification
from arduino.app_utils import *

flag = 0

# Create a classification stream with default confidence threshold (0.3)
classification_stream = VideoImageClassification()

# Callback when "crash helmet" is detected
def crash_helmet_detected():
    global flag
    flag = 1

classification_stream.on_detect("crash helmet", crash_helmet_detected)

# Callback for all classifications
def all_detected(results):
    global flag
    Bridge.call("cam_flag", flag)

    if flag == 1:
        print("helmet detected")
    else:
        print("helmet not detected")

    flag = 0

classification_stream.on_detect_all(all_detected)

App.run()
