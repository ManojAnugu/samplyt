from flask import Flask

app=Flask(__name__)


def manoj():
    return 'Namaste'
app.add_url_rule('/manoj','manoj',manoj)

if__name__=='__main__':
    app.run(debug=True)