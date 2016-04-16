import uuid
import common.datetime
from common.database import Database
from models.post import Post

class Blog:

	def __init__(self, author, title, description, author_id, _id=None):
		self.author = author
		self.author_id = author_id
		self.title = title
		self.description = description
		self._id = uuid.uuid4().hex if _id is None else _id

	def new_post(self, title, content, date=datetime.datetime.utcnow()):
		post = Post(blog_id=self._id,
					title=title,
					content=content,
					author=self.author,
					created_date=created_date)
		post.save_to_mongo()

	def get_posts(self):
		return Post.from_blog(self._id)

	def save_to_mongo(self):
		Database.insert(collection='blogs',
						data=self.json())

	def json(self):
		return {
			'author': self.author,
			'title': self.title,
			'description': self.description,
			'author_id': self.author_id,
			'_id': self._id
		}

	@classmethod
	def from_mongo(cls, _id):
		blog_data = Database.find_one(collection='blogs',
										query={'_id': _id})
		return cls(**blog_data)

	@classmethod
	def find_by_author_id(cls, author_id):
		blogs = Database.find(collection='blogs',
								query={'author_id': author_id})
		return [cls(**blog) for blog in blogs]