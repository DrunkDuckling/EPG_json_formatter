from flask import Flask, json, request
import datetime

test = 'Server Used for EPG data; create a post request with relevant data to get results.'

api = Flask(__name__)

# Program function; Used to manage each day and structure them correctly
def refactore(res):
    
    # Variables (bool) for new lines and if a day starts no shows or day starts with an ending of a show
    newLine = False
    meh = False
    
    # String contaning the full week of programs
    week = ''
    # Used if no program is on.
    noAir = 'Nothing aired today'
    
    # Loads json file so it can be worked with
    json_string = json.loads(res)
    
    # Go though each day in a for loop.
    for day in json_string:
        # Reset program each day; clean slate
        program = ''
    
        # Go though each item in the current day in the loop
        for value in json_string[day]:
    
            if(value["state"] == 'begin'):
                program += value['title'] + ' '
            
            # If the day only contains 1 one less items there might not be a reason to add anything
            if(len(json_string[day]) <= 1 and value["state"] == 'end'):
                meh = True  
            else: meh = False          
            
            # Get the first item from the day if it is an ending add it to week and continue to next loop
            if(value == json_string[day][0] and value['state'] == 'end'):
                newLine = False
                week += str(datetime.timedelta(seconds=value['time'])) + ' \n'
                # moves on to next loop "skipping" remainder
                continue
            # Get last item in day; if a show begins as last program of day, no new line.
            if(value == json_string[day][-1] and value['state'] == 'begin'):
                newLine = True
    
            # Add the times from the current state 'Begin'
            if(value['state'] == 'begin'):
                program += str(datetime.timedelta(seconds=value['time'])) + ' - '
            # Only add a comma "," if the program is not last
            if(value["state"] == 'end' and value == json_string[day][-1]):
                program += str(datetime.timedelta(seconds=value['time']))
            elif(value["state"] == 'end'):
                program += str(datetime.timedelta(seconds=value['time'])) + ', '
            
            # Add the  slash "/" if the program is not the last of the day
            if(value["state"] == 'end' and value == json_string[day][-1]):
                continue
            elif(value["state"] == 'end'):
                program +=  ' / '
    
        # Add the day to the string
        week += day + ': '
    
        if(meh or len(json_string[day]) == 0):
            week += noAir
        else:
            week += program
        if(not newLine):
            # Create a new line so there is proper structure in response
            week += ' \n'
        
    return week

# start: Primary function; the one called though the API
@api.route('/', methods=["POST", "GET"])
def get_data():
  if request.method == "GET":
    return test
  if request.method == "POST":
    return refactore(request.data)

if __name__ == '__main__':
    api.run() 