__author__ = 'jhuang'
import datetime

header = 'Subject,Start Date,Start Time,End Date,End Time,All Day Event,Reminder On/Off,Reminder Date,Reminder Time,Meeting Organizer,Description,Location,Private'
# Schedule html following certain format assumptions
sourcehtml = 'third_party/example.html'
EVENT = 'READEVENT'
DAY = 'READDAY'
PREFIX = 'style="font-size: 1.25em;">'
SUFFIX = '</span>'

def makecsv():
    f = open('schedule.csv', 'w')
    f.write(header)
    f.write('\n')

    def comma():
        f.write(',')

    mode = EVENT  # READDAY or READEVENT

    html = open(sourcehtml, 'r')
    # Find events interested (Voice recitals for now)
    for line in html:
        parts = line.split()
        if not parts:
            continue
        if parts[0] == '<td' and mode == EVENT:
            mode = DAY
            day = parts[len(parts) - 1][:parts[len(parts)-1].index('<')]
            day += '/%d' % datetime.datetime.now().year  # Assume current year
        elif parts[0] == '<td' and mode == DAY:
            mode = EVENT
        if mode == EVENT:
            if PREFIX not in line:
                continue
            if 'Voice' not in line and 'voice' not in line:
                continue
            alldata = line[line.index(PREFIX)+len(PREFIX):line.index(SUFFIX)]
            data = alldata.split(',')
            time = data[0]
            subject = data[1]
            description = data[2]
            location = data[4]

            f.write(subject)
            comma()
            f.write(day)
            comma()
            f.write(time)
            comma()
            for _ in range(7):
                comma()
            f.write(description)
            comma()
            f.write(location)
            comma()
            f.write('\n')
    f.close()


if __name__ == '__main__':
    makecsv()
