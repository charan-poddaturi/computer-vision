import cv2
image = cv2.imread('trial.jpeg')
if image is None:
    print("Error: Could not read the image.")
else:
    h, w, c = image.shape
    print(f"Image dimensions: {w}x{h}, Channels: {c}")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    if gray is not None:
        print("image converted to grayscale, do you want to see?")
        uin = input("Enter 'yes' or 'no': ")
        if uin.lower() == "yes":
            cv2.namedWindow('Gray Image', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Gray Image', 600, 400)
            cv2.imshow('Gray Image', gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("Saving the grayscale image as 'trial_gray.jpeg'...")
        else:
            print("Okay, not displaying the image.")
            print("Saving the grayscale image as 'trial_gray.jpeg'...")
cv2.imwrite('trial_gray1.jpeg', gray)