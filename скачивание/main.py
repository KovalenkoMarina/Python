import requests

img_url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/P.t.altaica_Tomak_Male.jpg'
video_url='https://youtu.be/qxWByNcV_DM'


def download_img(url=''):

    try:
        response = requests.get(url=url)

        with open('скачивание/req_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Img successfully downloadee!'

    except Exception as _ex:
        return 'Upps... Check the URL please!'

def download_video(url=''):

    try:
        response = requests.get(url=url)

        with open('скачивание/req_video.mp4', 'wb') as file:
            file.write(response.content)

        return 'Img successfully downloadee!'

    except Exception as _ex:
        return 'Upps... Check the URL please!'        

def main():
    # print(download_img(url=img_url))
    print(download_video(url=video_url))

if __name__ == '__main__':
    main()
