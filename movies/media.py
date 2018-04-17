import webbrowser


class Movie ():
    '''Class Movie Descripition:

    def __init__ : Intializes varaibles to assinged.
    -self.title = movie_title(STR): requires a string
    -self.storyline = movie_storyline(STR): requires a string
    -self.poster_image_url = poster_image(STR): requires a
     url from a website wrapped in a string
    -self.trailer_youtube_url = trailer_youtube(STR):
     requires a link from youtube url wrapped in a string

    def show_trailer : Opens web browser to,
    show trailer by clicking a image. '''

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
