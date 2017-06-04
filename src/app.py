from flask import Flask, request, session, redirect, render_template, flash, jsonify
from modules.database import Posts, Users, Comments, session_db
from hashlib import sha256
from modules import config, md, comments, posts

app = Flask(__name__)
app.secret_key = 'G\x8f\xee[N\x1b\x9a\x19\x16\nN\x00\xb3\x11\x0f\x08\xbfi\xd8\x14\x03o:\xfa'

@app.route('/')
def index_page():
    return render_template("index.html", posts=posts.return_post_list())

@app.route('/posts/<int:post_id>')
def posts_page(post_id):
    comments_list = comments.return_comment_list(post_id);
    post = posts.return_particular_post(post_id)
    return render_template("post.html", post=post, comment_list=comments_list)

@app.route('/page_admin')
def page_admin():
    if (not session.get('logged_in')):
        return redirect('/login')
    return render_template("page_admin.html")

@app.route('/add_post', methods=['POST'])
def add_post():
    posts.add_post(request.form['post_title'], request.form['post_text'])
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

@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    like_number_temp = session_db.query(Posts).filter(Posts.id == post_id).first().likes_number
    session_db.query(Posts).filter_by(id = post_id).update({'likes_number' : like_number_temp+1})
    session_db.commit()

    return jsonify({
    'likes_number' : session_db.query(Posts).filter(Posts.id == post_id).first().likes_number
    })

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comments.add_comment()

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/about')
def about():
    return render_template("about.html")

if ( __name__ == "__main__"):
    app.run(debug=True, host='0.0.0.0', port=5000);
