# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# movie name
name = input("Enter the movie you are looking for: ")

# searching the movie
search = ia.search_movie(name)

# printing the result
for i in search:
    print(i)