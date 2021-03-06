import tornado.web
from models.post import Post

class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("blog_user")
        if not user_id: return None
        #return self.db.get("SELECT * FROM user WHERE id = %s", int(user_id))
        return Post.select().where(Post.id == int(user_id))
