import cv2 as cv

video = cv.VideoCapture('highway.mp4')

if (video.isOpened() == False):
    print('Hubo un error al abrir el archivo')
else:
    fps = video.get(5)
    print('Cuadros x segundos', fps)
    frame_count = video.get(7)
    print('Numero de cuadros', frame_count)

    while (video.isOpened()):
        ret, frame = video.read()
        if ret == True:
            cv.imshow("Frames del video", frame)
            key = cv.waitKey(20)
            if key == ord('q'):
                break

        else:
            break
cv.destroyAllWindows()
