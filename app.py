from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Posts

app = Flask(__name__)
engine = create_engine()
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
def index_page():
    return render_template("index.html", posts=session.query(Posts).all())

if ( __name__ == "__main__"):
    app.run();
