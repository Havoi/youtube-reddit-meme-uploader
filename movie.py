from moviepy.editor import *

from moviepy.editor import *
def makemovie():
    files = ['Images/1.png']
    clip = ImageSequenceClip(files,fps= 0.05) 
    audioclip = AudioFileClip("1.mp3")
    videoclip = clip.set_audio(audioclip).subclip(0, 20)
    videoclip.write_videofile("video.mp4", fps = 1)