current_movies = {'The Grinch': '11:00', 'Avatar 2': '16:15', 'Thor, Love and Thunder': '19:00', 'All i want for Christmas': '22:30'}

print("We're showing the following movies\n")

for key in current_movies:
    print(key, "\n")

movie = input("What movie do you want to watch?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, " is playing at ",showtime)

