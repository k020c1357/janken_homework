import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    rps_pattern = {'グー': 1, 'チョキ': 2, 'パー': 3}
    res = {'computer': '', 'user': '', 'result': ''}

    user_choice = request.args.get('user','')

    if user_choice:

        user = rps_pattern[user_choice]
        computer = random.randint(1, 3)

        if user == computer:
            result = 'アイコ'
        else:
            if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
                result = "勝つ"
            else:
                result = "負け"
        res = {'computer': computer, 'user': user, 'result': result}

    return render_template('app.html', res=res)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
