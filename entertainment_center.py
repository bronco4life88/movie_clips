import fresh_tomatoes
import media

force_awakens = media.Movie("Force Awakens",
                        "Story of Rey journey to the force",
                        "https://pre00.deviantart.net/e1f4/th/pre/f/2016/118/b/6/star_wars_force_awakens_fan_poster_by_mevans2574-da0jvhs.png",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

new_hope = media.Movie("A New Hope",
                     "Story of a farm boy that turns hero",
                     "https://zrockr.com/user-files/uploads/2015/11/z114-671x1024.jpg",
                     "https://www.youtube.com/watch?v=1g3_CFmnU7k")

rogue_one = media.Movie("Rogue One",
                        "Story to find the death star plans",
                        "https://vignette.wikia.nocookie.net/starwars/images/5/58/Dolby_Rogue_One_poster.jpg/revision/latest?cb=20171029144953",
                        "https://www.youtube.com/watch?v=Wji-BZ0oCwg")

last_jedi = media.Movie("Last Jedi",
                       "storyline",
                       "https://lumiere-a.akamaihd.net/v1/images/sb_teaser2_1-sht_v3a_online_lg_44ecdb4e.jpeg?region=0%2C0%2C810%2C1200",
                       "https://www.youtube.com/watch?v=zB4I68XVPzQ")

empire = media.Movie("Empire Strikes Back",
                      "storyline",
                      "https://images-na.ssl-images-amazon.com/images/I/51C0cpp4d%2BL.jpg",
                      "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

return_of_the_jedi = media.Movie("Return of the Jedi",
                                 "storyline",
                                 "https://images-na.ssl-images-amazon.com/images/I/51UdiBUkerL.jpg",
                                 "https://www.youtube.com/watch?v=7L8p7_SLzvU")

movies = [force_awakens,new_hope,rogue_one,last_jedi,empire,return_of_the_jedi]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
