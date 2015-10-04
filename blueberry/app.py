from flask import Flask, render_template, g
import models as m

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
DATABASE = 'database.db'

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/signup', methods=['POST']")
def signup():
    userInfo = (email, password)
    user = m.User(userInfo[0], userInfo[1])
    m.db.add(user)
    m.db.session.commit()



if __name__ == "__main__":
    app.run()

def setupDB():
    user = m.User('Jesse', 'j@example.com')
    m.db.session.add(user)
    m.db.session.commit()

    scholarship = m.Scholarship('Super Math Student', 100, 'Mathematics')
    m.db.session.add(scholarship)
    m.db.session.commit()

    extracurricular = m.Extracurricular('Soccer', 50, 'Sports')
    m.db.session.add(extracurricular)
    m.db.session.commit()

    contest = m.Contest('AMC 10', '100', 'Test', 'Mathematics')
    m.db.session.add(contest)
    m.db.session.commit()



def readDB():
    print(m.User.query.all())
    print(m.Scholarship.query.all())
    print(m.Extracurricular.query.all())
    print(m.Contest.query.all())

