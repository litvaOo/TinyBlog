from flask import Flask, request, session, redirect, render_template, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.database import Base, Posts, Users
from hashlib import sha256
from modules import config, md

app = Flask(__name__)
engine = create_engine(config.Config.buildConnectionString())
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session_db = DBSession()
app.secret_key = 'G\x8f\xee[N\x1b\x9a\x19\x16\nN\x00\xb3\x11\x0f\x08\xbfi\xd8\x14\x03o:\xfa'

@app.route('/')
def index_page():
    return render_template("index.html", posts=session_db.query(Posts).order_by(Posts.id.desc()))

@app.route('/posts/<int:post_id>')
def posts_page(post_id):
    return render_template("post.html", post=session_db.query(Posts).filter(Posts.id == post_id).first())

@app.route('/page_admin')
def page_admin():
    if (not session.get('logged_in')):
        return redirect('/login')
    return render_template("page_admin.html")

@app.route('/add_post', methods=['POST'])
def add_post():
    new_post = Posts(request.form['post_title'], md.markdown_to_html(request.form['post_text']))
    session_db.add(new_post)
    session_db.commit()
    flash("Post_added")
    return redirect('/')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if (request.method == 'GET'):
        return render_template("login.html")
    else:
        if (session_db.query(Users).filter(Users.login == request.form['login'] and Users.password == sha256(request.form['password'])).first()):
            session['logged_in'] = True
            if (session_db.query(Users).filter(Users.login == request.form['login'] and Users.isadmin == True).first()):
                return redirect('/page_admin')
            else:
                flash("You're not an admin, redirecting to the posts page")
                return redirect("/")
        else:
            flash("Wrong login, check the credentials")
            return redirect('/login')

@app.route('/test')
def tests():
    return render_template("layout.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/about')
def about():
    return render_template("about.html")

if ( __name__ == "__main__"):
    app.run(debug=True, host='0.0.0.0');
