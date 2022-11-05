# DhruvTara-Object-Detection-through-Voice-Recognition-for-visually-impaired

Abstract :
Nearly all practical applications, including autonomous navigation, visual systems, face recognition, and more, rely on object detection. In this paper, object 
detection and speech recognition are combined to help visually impaired people who want to use voice commands to find a certain object. People who are blind or 
visually challenged can move more independently if they are aware of their surroundings. With the use of the OpenCV libraries, a model has been implemented, and 
good results have been obtained. In this paper, a thorough review of object detection employing region-based conventional neural network (CNN)- based learning 
systems for practical applications has been conducted. This study examines the various object identification processes utilizing YOLOV4 object detection techniques 
and talks through detection, including a speech recognition system that was created by transcribing spoken language into text.

Introduction :
In our model, we divided our work in cost two parts i.e. speech recognition part and object detection part. Firstly, in speech recognition part, we give speech 
i.e. voice command as an input to our model wherein using  libraries such as speech recognition and pyttsx3 we convert the input speech to its text format. 
Herein, the user needs to speak the name of the required object he/she wants to search and then the required program would convert the name of the object 
to its text format. Then, the text-name is given as an input to the object detection part where we have used CNN model in which we are using YOLOV4 algorithm 
which makes the base for our object detection model, in which OpenCV library is used for the detection of the required object. The given text-input is matched 
with the dataset embedded in our model and then the camera is enabled to detect the object in the given environment or background. A bounding box is formed 
when the object is detected and then the model stops working.

For our specific model, we also build our own custom dataset which has 52 different types of objects with more than 20,000 images for the detection.

Hardware components :
1) Raspberry pi 4B
2) Raspberry pi case
3) Camera (Raspberry Pi NoIR Camera)
4) Microphone
5) Speaker
6) Battery (Lithium batteries)
7) Buzzer
8) Ultrasonic sensor ( ultrasonic sensor HC-SR04)



