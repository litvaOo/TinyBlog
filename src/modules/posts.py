from modules.database import Posts, Users, session_db

def return_post_list():
    return session_db.query(Posts).order_by(Posts.id.desc())

def return_particular_post(post_id):
    return session_db.query(Posts).filter(Posts.id == post_id).first()

def add_post(title, text):
    new_post = Posts(title, md.markdown_to_html(text))
    session_db.add(new_post)
    session_db.commit()
