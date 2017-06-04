from modules.database import Comments, session_db
from json import dumps


def add_comment(post_id, text):
    session_db.add(Comments(post_id, text))
    session_db.commit()
    return return_comment_list(post_id)

def return_comment_list(post_id):
    comment_list = list(session_db.query(Comments).filter(Comments.post_id == post_id))
    return comment_list

def carma_change(post_id, comment_id, direction):
    pass

add_comment(1, "random_text")
