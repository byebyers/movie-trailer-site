import byers_movie_site
import media


the_matrix = media.Movie(
	"The Matrix", 
	"A man living in a vitrual world.", 
	"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", 
	"https://www.youtube.com/watch?v=fY9UhIxitYM")

#the_matrix.show_trailer()

team_america = media.Movie(
	"Team America", 
	"A broadway actor finds himself in the fight against terrorism.", 
	"https://upload.wikimedia.org/wikipedia/en/5/53/Team_america_poster_300px.jpg", 
	"https://www.youtube.com/watch?v=RPBX47zSktc")

spirited_away = media.Movie(
	"Spirited Away", 
	"10 year old Chihiro stumbles upon a seemingly abandon amusement park.", 
	"https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG", 
	"https://www.youtube.com/watch?v=ByXuk9QqQkk")

super_troopers = media.Movie(
	"Super Troopers", 
	"Team of bored highway police find themselves in threat of being shutdown.", 
	"https://upload.wikimedia.org/wikipedia/en/1/19/Supertrooper.jpg", 
	"https://www.youtube.com/watch?v=2-9D2qUHN-E")

movies = [the_matrix, team_america, spirited_away, super_troopers]

'''In the function below we are to open the module open_movies_page from the file byers_movie_site. 
From there the parameter fpr open_movie_page is movies which takes it from it's assignement above.'''
byers_movie_site.open_movies_page(movies)
