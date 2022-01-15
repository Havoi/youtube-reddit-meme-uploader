import os
def remove():
    try:
        os.remove('./Images/1.png')
    except:
        pass
    try:
        os.remove('./video.mp4')
    except:
        pass