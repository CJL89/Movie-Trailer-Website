import webbrowser


# Class that contains all the different elements that are shown within the title of the movie.
class Movies():


    # Variables that have a fixed output:
    RATINGS = ["G", "PG", "PG-13", "R"]
    GENRES = ["Action", "Animation", "Comedy", "Documentary", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", ]
    
    
    # Variables that do not have a fixed output:
    def __init__(self, title, description, RATINGS, GENRES, director, writter, runtime, cast, review, image_poster, trailer):
        self.movieTitle = title
        self.movieDescription = description
        self.movieRating = RATINGS
        self.movieGenre = GENRES
        self.movieDirector = director
        self.movieWritter = writter
        self.movieRuntime = runtime
        self.movieCast = cast
        self.movieReview = review
        self.moviePoster = image_poster
        self.movieTrailer = trailer


    # Opens the link to Youtube to show the trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
