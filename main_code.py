from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__, template_folder=".")

@app.route('/', methods=['GET', 'POST'])
def startscreen():
    return render_template('usersdata.html')

@app.route('/usersdata', methods=['GET', 'POST'])
def usersdata():
    area = request.form['area']
    city = request.form['city']
    anstime = time(area, city)
    if anstime == "0":
        return "What a hell?! your data is incorrect"
    answer = f'Time, you was looking for, is {anstime}'
    return answer

def time(area, city):
    url = f'http://worldtimeapi.org/api/timezone/{area}/{city}'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        print(data)
        anstime = data['datetime']
        return anstime
    return "0"

if __name__ == '__main__':
    app.run(debug=True)
