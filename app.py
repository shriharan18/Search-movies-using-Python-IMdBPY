# This code was written by Shreeharan for the YouTube Channel Stark Intelligence : https://www.youtube.com/starkintelligence
import imdb     # importing the module

# creating instance of IMDb
ia = imdb.IMDb()

# movie name
name = input("Enter the movie you are looking for: ")

# searching the movie
search = ia.search_movie(name)

# printing the result
for i in search:
    print(i)
