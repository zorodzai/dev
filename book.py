class Book:
	def __init__(self, title, author=None):
		self.title = title
		self.author = author

	def print_info(self):
		print(self.title)
