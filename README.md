
# Mousetracking

<h1> Research Study for recognizing human emotions</h1>

The objective is to determine the emotion of a person taking a survey by tracking mouse and keyboard. For example, if the response time between opening the page and answering is long, the person is not confident. The data collected will be fed to Machine Learning algorithms to visualize the data and recognize emotions from them.


Run interview.py and open the page "/admin" (for admins) it at the local host with port connected.

To begin the survey, the admin logs in to the system, adds the candidate name and details. Press record to start recording.
Press playback to see the user's recorded survey. A simple admin page is shown:

![Alt text](/screenshots/Screenshot5.png)

The admin can then place the candidate on the chair with all sensors (eyetracking, ECG, etc. ) when the browser shows like:
![Alt text](/screenshots/Screenshot6.png)

The survey includes questions of different types including:

<h3> Text based: </h3>

![Alt text](/screenshots/Screenshot1.png)


<h3> Rating based: </h3>

![Alt text](/screenshots/Screenshot2.png)


<h3> Audio/Video based: </h3>

![Alt text](/screenshots/Screenshot4.png)


<h3> Image based: </h3>

![Alt text](/screenshots/Screenshot3.png)

The mouse- tracking done in the backend gets data in the format:

![Alt text](/screenshots/Screenshot7.png)


This survey can be played back in the same motion as the user answered.




<h3> FILES: </h3> </br>

interview.py - (main page) opens the admin page and generates questions or playback as per the admin response </br>
admin.py - checks admin ID password </br>
Quiz.py - generates quiz questions based on the quiz ID given by admin</br>
db.py - connects to the MySQL database</br>
dbase.py - functions for accessing and modifications in the database</br>
model.py - functions to create user directory, record and playback</br>
keym.py - functions to record the mouse events</br>
playback.py - fucntions to playback the entire survey </br>


<h3> FOLDERS: </h3> </br>
Question- List of all questions </br>
Quiz- quiz ID linking questions </br>
Static- audios/videos/images </br>
Subjects- directory for each subject taking the survey  </br>
Templates- HTML templates for the each quiz question </br>




