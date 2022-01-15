# webserver
#----------------------------------------------------------------
import photo_and_video_remover
import Image_Downloader
import Photo_renamer
import image_resizer
import movie
import upload
YOUTUBE = upload.credentials()
I = 1
def main():
    try:
        photo_and_video_remover.remove()
        Image_Downloader.downloader(I)
       
        Photo_renamer.multi_filename_change() 
        image_resizer.resize()  
        movie.makemovie()
        upload.upload(YOUTUBE)
        print("UPLOADED!")
    except Exception as e:
        if e == " name 'GetPreviousHashes' is not defined:":
            print("UPLOADED!")
        else:
            print("ERROR: ",e)


while True:
    main()
    I+=1