# # 1. Movie Ratings Analyzer 
# # Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...]. Compute 
# # the average rating, find the highest-rated movie, and list all movies with rating above the 
# # average. 
movies =[]
s_rate =0

movie_input =input("Enter movies and ratings separated by spaces(eg.movie1-10 movie2-5):")

movie_input =movie_input.replace(","," ")
entries = movie_input.split()
# print(entries) #['a-5', 'b-6']
for item in entries:
    name, rating = item.split("-")
    rating = float(rating)
    s_rate += rating
    movies.append((name, rating))

print("Entered movies and ratings:",movies)

average_rating =s_rate/len(movies)

h_rate =movies[0]
for movie in movies[1:]:
    if movie[1] >h_rate[1]: 
        h_rate = movie

above_avg = []
below_avg = []
for name, rating in movies:
    if rating>average_rating:
        above_avg.append(name)
    elif rating<average_rating:
        below_avg.append(name)

print(f"Average rating:{average_rating}")
print(f"Highest rated movie:{h_rate[0]}")
print(f"Movies above average:{above_avg}")
print(f"Movies below average:{below_avg}")