import fresh_tomatoes
import media

force_awakens = media.Movie("Force Awakens",
                            "Story of Rey journey to the force",
                            "https://goo.gl/8k2q68",
                            "https://www.youtube.com/watch?v=sGbxmsDFVnE")

new_hope = media.Movie("A New Hope",
                       "Story of a farm boy that turns hero",
                       "https://goo.gl/QozA2Q",
                       "https://www.youtube.com/watch?v=1g3_CFmnU7k")

rogue_one = media.Movie("Rogue One",
                        "Story to find the death star plans",
                        "https://goo.gl/anpsYo",
                        "https://www.youtube.com/watch?v=Wji-BZ0oCwg")

last_jedi = media.Movie("Last Jedi",
                        "storyline",
                        "https://goo.gl/oAgTiB",
                        "https://www.youtube.com/watch?v=zB4I68XVPzQ")

empire = media.Movie("Empire Strikes Back",
                     "storyline",
                     "https://goo.gl/5ZEipF",
                     "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

return_of_the_jedi = media.Movie("Return of the Jedi",
                                 "storyline",
                                 "https://goo.gl/AMsqCE",
                                 "https://www.youtube.com/watch?v=7L8p7_SLzvU")

movies = [force_awakens new_hope rogue_one last_jedi empire return_of_the_jedi]
'#Creates a list for each movie'

fresh_tomatoes.open_movies_page(movies)
'#calls the fresh_tomatoes.py and sends all the data to the created html file.'
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
