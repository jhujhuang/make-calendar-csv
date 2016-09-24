# make-calendar-csv
A small script that I wrote to make a calendar (actually, a `.csv` file that can be imported as a calendar) with all "Voice" recitals at JHU Peabody.

Last semester (Spring 2016) I took Music Theory III - Songs, which required us to listen to two concerts including at least one voice recitals. The recitals were listed at http://www.peabody.jhu.edu/events/recitals.html which I downloaded as example.html in this repository. It was not the most convenient to plan ahead by looking at the original webpage and CTRL+F search for voice, since there were quite many voice recitals among which I just needed to choose to go to one when I feel like to, maybe 30 mins before it starts. I am used to keep every event I *may* go to organized in google calendar, so I thought it would be nice to have the recitals I'm interested in as a calendar on its own.

This script generates a `.csv` file that can be imported to Google Calendar (and other calendar apps). To run, simply do `$ python makecsv.py` which will write a file called `schedule.csv`.
