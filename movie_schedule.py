movie_schedule = {
    'The Hulk':'11:00am',
    'Iron Man':'1:00pm',
    'Captain America': '3:00pm',
    'Thor':'5:30pm'
}
print("Here is the movie schedule for today:")
for key in movie_schedule:
    print(key)
    
movie = input("Which movie do you want to see?\n")

showtime = movie_schedule.get(movie)

if showtime == None:
    print("Movie is not playing")
else:
    print(movie, 'is playing at', showtime)
    