import winsound
from plyer import notification

notification.notify(
    title="Hydration Reminder",
    message="Time To Drink Water",
    app_icon="Paste the Path Of Your Preferred icon",#the imgae should be in .ico format
    timeout=5
)
winsound.PlaySound(
    "paste the path of your prefered Audio",winsound.SND_FILENAME)

"""the audio file should be in .wav and paste the path inside the parathesis
 if you get double paranthesis remove one set of paranthesis"""