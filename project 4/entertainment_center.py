# Lesson 3.4: Make Classes
# Mini-Project: Movies Website
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import media
import fresh_tomatoes
""" this file will populate the `Movie` model with some of my favorite movies
The images I used were from the official Imdb site
"""
deadpool2 = media.Movie('Deadpool 2','Foul-mouthed mutant mercenary Wade Wilson (AKA. Deadpool), brings together a team of fellow mutant rogues to protect a young boy of supernatural abilities from the brutal, time-traveling mutant, Cable.','https://www.bleedingcool.com/2018/05/02/5-new-deadpool-2-posters/deadpool-2-poster-5/#main','https://youtu.be/20bpjtCbCz0')
avengers_infinity_war = media.Movie('Avengers Infinity Wars','The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.','https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg','https://www.youtube.com/watch?v=6ZfuNTqbHE8')
thor_ragnarok = media.Movie('Thor Ragnarok','Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.','https://ia.media-imdb.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg','https://www.youtube.com/watch?v=ue80QwXMRHg')
spiderman_homecoming = media.Movie('Amazing Spiderman','Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man, and finds himself on the trail of a new menace prowling the skies of New York City.','https://ia.media-imdb.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_QL50_SY1000_CR0,0,658,1000_AL_.jpg','https://www.youtube.com/watch?v=rk-dF1lIbIg')
black_panthers = media.Movie('Black Panther','''T'Challa, the King of Wakanda, rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake.''','https://ia.media-imdb.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL__QL50.jpg','https://www.youtube.com/watch?v=xjDjIWPwcPU')
jumanji = media.Movie('Jumanji: Welcome to the Jungle','Four teenagers are sucked into a magical video game, and the only way they can escape is to work together to finish the game.''','https://ia.media-imdb.com/images/M/MV5BODQ0NDhjYWItYTMxZi00NTk2LWIzNDEtOWZiYWYxZjc2MTgxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg','https://www.youtube.com/watch?v=2QKg5SZ_35I')
blockers = media.Movie('Blockers','Three parents try to stop their daughters from losing their virginity on prom night.','https://ia.media-imdb.com/images/M/MV5BMjE0ODIzNjkzMl5BMl5BanBnXkFtZTgwODQ3MzU4NDM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg','https://www.youtube.com/watch?v=uMDVa4yoCWw')
movies = [deadpool2, avengers_infinity_war, thor_ragnarok, spiderman_homecoming, black_panthers, jumanji,blockers]
fresh_tomatoes.open_movies_page(movies)
