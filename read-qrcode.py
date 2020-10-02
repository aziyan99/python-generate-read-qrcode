import cv2
import os
import sys


def main():
    # get current dir
    current_dir = os.getcwd()
    # set target dir
    target_dir = current_dir + "img/ezy.png"

    # read img
    img = cv2.imread(target_dir)
    # init detector
    detector = cv2.QRCodeDetector()
    # detect and decode
    data, bbox, straight_qrcode = detector.detectAndDecode(img)

    # if there is qrcode
    if bbox is not None:
        print(F"QRCode data:\n{data}")

        # display the image with line
        # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
            # draw line
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

    # display result
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
