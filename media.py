import webbrowser

class Movie():
	'''This function is the blueprint for the movie assignement in entertainment_center. 
	Here we initialize the funtion by assigning the parts of the paramenter per movie.'''
	def __init__ (self, movie_title, movie_storyline, post_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = post_image
		self.trailer_youtube_url = trailer_youtube


	def show_trailer(self):
		'''This funtion takes in the specific movie and opens the parameter self.trailer_youtube_url in a webbrowser. 
		This works because that parameter is a web address to a youtube video.'''
		webbrowser.open(self.trailer_youtube_url)