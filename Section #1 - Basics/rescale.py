import cv2 as cv

# Change existing videos
def rescaleFrame(frame, scale=.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Only works for live videos!!
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# # Resize Images
# img = cv.imread('../Resources/Photos/cat.jpg')
# resized_image = rescaleFrame(img, scale=1.5)
# cv.imshow('Cats', img)
# cv.imshow('Cats Resized', resized_image)

# cv.waitKey(0)

# Resize Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read() 
    frame_resized = rescaleFrame(frame)

    if isTrue:
        cv.imshow('Video Resized', frame_resized)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()