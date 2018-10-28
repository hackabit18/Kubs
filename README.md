# Audan (AUDience ANalysis)

## Idea

Theme *-* ***AI in Educational Discourse***

Problem Statement

Are tests, viva or examinations sufficient to evaluate a classroom? Limitations with present teaching-learning process :

- Difficult to find root of the problem as these reports just present general picture.
- Time consuming.
- Overshadows one’s interest.

The idea is to enhance the teaching-learning process and make it more personalized by analyzing the emotions of students in a class.

- Can be used as a real-time feedback for teachers.
- Easily spot exceptional/abnormal behavior 
- Could be helpful in finding one’s interests.

Approach

Our approach is to use existing face & emotion detectors, like Azure’s Vision API or Google Cloud Vision API, to detect collective emotion of an audience to use as a quantitative measure of their response towards the discourse.  With this information at hand, a number of accurate inferences can be made and actions can be taken to improve if the audience is losing interest. No new hardware is needed because good cameras already exists in classrooms, talks, and presentation that focuses on the audience and can be readily integrated with our system to generate analysis reports. An extended analysis also lets one see each of the detected person’s age & emotion.

*Why emotions?*

Facial emotions play an important role in everyday interaction of people with others. Late Psychology research has demonstrated that the people express their feelings fundamentally through outward appearances.


## Tech Stack

Some general steps :

- Face Detection using Deep ConvNets ( *Delegated to Azure API* )
- Emotion Classification ( *Azure detects 7 emotions* )
- Analysis and Feedback ( *Correlation across different attributes like Age, Gender, Strength and Emotions* )

Tools Used :

- Microsoft Azure API - For face detection
- OpenCV - Frames decomposition
- Python Backend - To determine correlation across different attributes
- Flask Server - For integration
- React - Web App for displaying analysis reports


## Application

We have a React frontend that allows users to drop in their video for analysis and view the stats as interactive visualizations using Plotly.js. The backend engine uses OpenCV to extract frames from the video at 5 fps and sends it to Azure to get the emotion of the detected faces. And while all this is happening, we use a socket connection to emit progress as each frame’s processing is completed. At the end, the entire analysis report is emitted and displayed as interactive plots. 


## Future Scope
- Optimize video processing in order to enable live feedback to speakers
- Making desktop software for educational institutes to monitor the lectures/classes.
- Sentiment Analysis of crowd to determine upcoming reaction of the audience, e.g, in Malls, Police Station, et al.


## Copyright - MIT License 

