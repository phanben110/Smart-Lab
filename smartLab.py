import cv2
import numpy as np
import matplotlib.pyplot as plt
import define as de
import calculatorCheckTable as cal
import array as arr
import csv

video = "22.mp4"
video = "24.mp4"
video = "01.mp4"

#video = "33.avi"


def saveDataToFileCsv(data):
    with open('TraMyDinh.csv', mode='w') as TraMyDinh:
        TraMyDinh = csv.writer(TraMyDinh, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        TraMyDinh.writerow(data)


people = [0, 0, 0, 0, 0, 0, 0]
numbers_array = arr.array('i', people)


def checkAngleForTable():
    cap = cv2.VideoCapture(video)
    cv2.namedWindow("Image")
    img_counter = 0
    while 1:
        while True:
            ret, frame = cap.read()
            # cv2.imshow("Image", frame)
            plt.figure()
            plt.imshow(frame)
            plt.show()  # display it
            break


def angleTable(coordinatesX, coordinatesY, R, picture):
    cv2.circle(picture, (coordinatesX, coordinatesY), R, (0, 255, 0), 5)


def creatCenterPoint(_X, _Y, _W, _H, imag):
    cv2.circle(imag, (int(_X + _W/2), int(_Y + _H/2)), 1, (0, 255, 0), 5)
    C = (_X + _W/2,  _Y + _H/2)
    return C


def paintLineTable(table, img):
    start_point = (table[0][0], table[0][1])
    end_point = (table[1][0], table[1][1])
    color = (255, 0, 255)
    thickness = 5
    cv2.line(img, start_point, end_point, color, thickness)


def checkPointWithTable(table, C, img):
    count = 0 
    for i in range(7):
        check = cal.checkCondition((cal.distanceAH(table[i], cal.solvePointH(table[i], C))), (cal.distanceBH(
            table[i], cal.solvePointH(table[i], C))), cal.distanceAB(table[i]), (cal.distanceFromCtoAB(table[i], C)), de.distanceValue)
        if check == True:
            print("OK OK OK OK")
            print(cal.solvePointH(table[i], C))
            color = (255, 0, 255)
            thickness = 5
            count += 1 
            print (f"table {i+1}") 

            people[i] = people[i] + 1
           
            end = cal.solvePointH(table[i], C)

            start_point = (int(end[0]), int(end[1]))
            end_point = (int(C[0]), int(C[1]))
            cv2.line(img, start_point, end_point, color, thickness)
            # label = "Table " + str(i+1) + ": "+ str(people[i]) + " people"
            # font = cv2.FONT_HERSHEY_PLAIN
            # color = (100, 100, 255)
            # cv2.putText(img, label, (start_point[0]-100, start_point[1]-150), font, 2, color, 2)

        # Access camera and take, save photo
    print ( f"people { count} "  )
    return count 

def doing():
    cap = cv2.VideoCapture(video)

    cv2.namedWindow("Image")
    img_counter = 0
    while 1:
        #while True:
           #ret, frame = cap.read()
            #height = frame.shape[0]/2 
            #weight = frame.shape[1]/2
            #print ( weight  )
            #print ( height ) 
            ##cv2.imshow("Image", frame)
            ##cv2.waitKey(100)
            #if not ret:
            #    break
            #    # SPACE pressed to take
            #img_name = "ben_dep_trai_{}.png".format(img_counter)
            #cv2.imwrite(img_name, frame)
            #print("{} written!".format(img_name))
            #break
        # cap.release()
        # cv2.imshow('Image', frame)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # cv2.waitKey(1)

        # Load Yolo

        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        classes = []
        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1]
                         for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        # Loading image
        #img = cv2.imread("ben_dep_trai_0.png")
        ret, img = cap.read()
        img = cv2.resize( img  , ( 1600 , 900 ) )  # resize for 1.2 real
        # img = cv2.resize(img, None, fx=0.4, fy=0.4)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(
            img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        print(indexes)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]

            if label == 'people':
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                creatCenterPoint(x, y, w, h, img)
                checkPointWithTable(
                    de.TABLE, creatCenterPoint(x, y, w, h, img), img)
                # cv2.putText(img, label, (x + 50, y - 5), font, 1, color, 2)
                print ( i ) 

        #angleTable(de.coordinatesX1 ,de.coordinatesY1, de.R1, img)
        #angleTable(de.coordinatesX2, de.coordinatesY2, de.R2, img)
        #angleTable(de.coordinatesX3, de.coordinatesY3, de.R3, img)
        #angleTable(de.coordinatesX4, de.coordinatesY4, de.R4, img)
        #angleTable(de.coordinatesX5, de.coordinatesY5, de.R5, img)
        #angleTable(de.coordinatesX6, de.coordinatesY6, de.R6, img)
        #angleTable(de.coordinatesX7, de.coordinatesY7, de.R7, img)
        paintLineTable(de.table1, img)
        paintLineTable(de.table2, img)
        paintLineTable(de.table3, img)
        paintLineTable(de.table4, img)
        paintLineTable(de.table5, img)
        paintLineTable(de.table6, img)
        paintLineTable(de.table7, img)
        for i in range(7):
            cv2.putText(img, "Table" + str(i+1) + ": " + str(people[i]) + " people",
                        (de.TABLE[i][0][0] - 100, de.TABLE[i][0][1] - 150), font, 2, (255, 255, 255), 4)

        saveDataToFileCsv(people)

        for i in range(7):
            people[i] = 0
        #img = cv2.resize( img , ( 960 , 540 ) )  # resize for 1.2 real
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        plt.imshow(img)
        #cv2.waitKey(3000)

        # cv2.destroyAllWindows()
# checkAngleForTable()
# checkPointWithTable(de.TABLE, (3,4))
doing()

cv2.destroyAllWindows()
