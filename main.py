
from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer
import http.client
import json
import requests
print("This program takes the movies you like, the ones you don't, and the ones you are curious about if you will like or not. It uses Machine Learning with the data obtained from The Movie Database through an API to understand what you like and don't like. The data it uses to predict is the overview, genre, and director of each movie. It then predicts if you will like/probably like/probably not like/not like the movies you are curious about. As with all programs with Machine Learning, the more data (in our case, movies you like and don't) you can give the program, the better it will predict. As an added bonus, the program also predicts which top 20 rated movies on the entire database you will like. Please be careful to input a movie title as it is so that you get the movie you actually mean and the prgram doesn't throw an error. Happy Testing and Happy Watching! - Kaustubh")
print()
#APIKey I got by making a dev account at TMDB.
APIKey = ""




#empty lists designed to store user input and different parameters of the user's input

#Movies that the user likes and doesn't like go here
positive_titles = []

negative_titles = []

#The overview, genre IDs, and Director Name for each movies is stored here for training the machine.
training_texts = []

#Movies the user wants to know if he'll like or not based one the ones he knows he likes and dislikes
tobetested = []

#The overview, genre IDs, and Director Name for each movies is stored here for the machine to decide if it is a movie the user will like or not
tobetested_texts = []

#This array is for the titles of the top rated 20 movies on TMDB
mostpopular_titles = []

#The overview, genre IDs, and Director Name for the top 20 rated movies is stored here for the machine to decide if it is a movie the user will like or not
mostpopular_texts = []




#The following lines are for taking input for the user and populating the arrays initialized above. 
i = int(input("How many movies that you like are you entering? "))

for x in range(i):
  movieName = input("Enter the name of a movie you liked: ")
  positive_titles.append(movieName)

print()

i = int(input("How many movies that you don't like are you entering? "))

for x in range(i):
  movieName = input("Enter the name of a movie you didn't like: ")
  negative_titles.append(movieName)

print()

i = int(input("How many movies you're curious about are you entering?"))

for x in range(i):
  movieName = input("Enter the name of a movie you want to check: ")
  tobetested.append(movieName)

print()
print()
print()



#lists of movies to make testing easier and faster. You will have to uncomment this block and comment out the block above for using this. 
'''
negative_titles = ["Avatar", "1917", "Joker", "Inception", "Interstellar", "Inglourious Basterds", "The Platform", "Titanic", "The Wolf of Wall Street", "El Camino"]

positive_titles = ["Toy Story", "Big Hero 6", "Trolls World Tour", "Jumanji: The Next Level", "Ninja Turtles", "Tangled", "Despicable Me 2", "Finding Nemo", "Garfield", "Toy Story 2"]

tobetested = ["Alladin", "Frozen", "Coco", "Mad Max: Fury Road", "Pets 2", "Incredibles 2", "Sing", "Zootopia", "The Revenant", "Inside Out", "Ad Astra", "Trolls", "Shrek"]
'''


#Goes through the movies that the user likes and pulls the above mentioned parameters from TMDB to store in training_texts
for x in range(len(positive_titles)):
  directors = []
  movieName = positive_titles[x]
  httpRequest = "https://api.themoviedb.org/3/search/movie?include_adult=false&page=1&query="+movieName+"&language=en-US&api_key="+APIKey
  response = requests.get(httpRequest)
  data = response.json()
  training_texts.append(data["results"][0]["overview"])
  training_texts.append(str(data["results"][0]["genre_ids"]))

  movie_id = data["results"][0]["id"]
  httpRequest2 = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + APIKey + "&append_to_response=credits"
  response = requests.get(httpRequest2)
  data = response.json()
  hello = data["credits"]
  hello1 = hello["crew"]
  for x in hello1:  
    if x["job"] == "Director":  
        directors.append(x["name"]) 
  training_texts.append(str(directors))

#Goes through the movies that the user doesn't like and pulls the above mentioned parameters from TMDB to store in training_texts
for x in range(len(negative_titles)):
  directors = []
  movieName = negative_titles[x]
  httpRequest = "https://api.themoviedb.org/3/search/movie?include_adult=false&page=1&query="+movieName+"&language=en-US&api_key="+APIKey
  response = requests.get(httpRequest)
  data = response.json()
  training_texts.append(data["results"][0]["overview"])
  training_texts.append(str(data["results"][0]["genre_ids"]))

  movie_id = data["results"][0]["id"]
  httpRequest2 = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + APIKey + "&append_to_response=credits"
  response = requests.get(httpRequest2)
  data = response.json()
  hello = data["credits"]
  hello1 = hello["crew"]
  for x in hello1:  
    if x["job"] == "Director":  
        directors.append(x["name"]) 
  training_texts.append(str(directors))  

#Goes through the movies that the user likes and pulls the above mentioned parameters from TDMB to store in tobetested_texts
for x in range(len(tobetested)):
  directors = []
  movieName = tobetested[x]
  httpRequest = "https://api.themoviedb.org/3/search/movie?include_adult=false&page=1&query="+movieName+"&language=en-US&api_key="+APIKey
  response = requests.get(httpRequest)
  data = response.json()
  tobetested_texts.append(data["results"][0]["overview"])
  tobetested_texts.append(str(data["results"][0]["genre_ids"]))

  movie_id = data["results"][0]["id"]
  httpRequest2 = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + APIKey + "&append_to_response=credits"
  response = requests.get(httpRequest2)
  data = response.json()
  hello = data["credits"]
  hello1 = hello["crew"]
  for x in hello1:  
    if x["job"] == "Director":  
        directors.append(x["name"]) 
  tobetested_texts.append(str(directors))  

#Pulls the parameters for the current 20 top rated movies and puts them in mostpopular_texts
directors = []
httpRequest = "https://api.themoviedb.org/3/movie/top_rated?api_key=e20e035943ec00333eb2a1d09ea93a5c&language=en-US&page=1"
response = requests.get(httpRequest)
data = response.json()
bye = data["results"]
for x in bye:
  if x["overview"] != "" or x["genre_ids"] != "":
    mostpopular_titles.append(x["title"])
    mostpopular_texts.append(x["overview"])
    mostpopular_texts.append(str(x["genre_ids"]))
    movie_id = x["id"]
    httpRequest2 = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + APIKey + "&append_to_response=credits"
    response = requests.get(httpRequest2)
    data = response.json()
    hello = data["credits"]
    hello1 = hello["crew"]
    for x in hello1:  
      if x["job"] == "Director":  
        directors.append(x["name"]) 
    mostpopular_texts.append(str(directors))  






#Here I prepare an equivalent set of labels, to tell the machine
# that the first texts that came from movies the user liked are positive and the rest are negative. 
# When I feed these into the classifier, it'll use indices to match up 
# the texts and qualify what parameters are good and bad. 
training_labels = ["good"] * (3*len(positive_titles)) + ["bad"] * (3*len(negative_titles))




#The vectorizer is set up here: the first main component of machine learning
vectorizer = CountVectorizer(stop_words='english')

 
#Here I feed the data we have into the vectorizer so it can keep a 
# consistent mapping. 
vectorizer.fit(training_texts)


# Here I transform all of the training texts into vector form. Basically makes it a list of numbers because code makes decisions quantitatively
training_vectors = vectorizer.transform(training_texts)



#I also convert the texts we are going to test and classify as good and bad into vector form
test_texts = tobetested_texts
test_populartexts = mostpopular_texts
testing_vectors = vectorizer.transform(test_texts)
testing_vectors_popular = vectorizer.transform(test_populartexts)


#This is here the real machine learning happens as the code "connects the dots" between the training data and what is considered good and bad using the labels. 
classifier = tree.DecisionTreeClassifier()
classifier.fit(training_vectors, training_labels)



#Uses the connections the code made in previous steps to test each of the parameters of each movie the user wants to test and returns if the user will like/not like/probabaly like/probabaly not like based on the results.
likeDict = {
  "will like" : "",
  "will probably like" : "",
  "will probably not like" : "",
  "will not like" : ""
}
print("Out of the movies you wanted to test:")
print()
for i, movie in enumerate(tobetested):
  listFormat = [tobetested_texts[i*3], tobetested_texts[i*3+1], tobetested_texts[i*3+2]]
  vectorFormat = vectorizer.transform(listFormat)
  result = classifier.predict(vectorFormat)
  if result[0] == 'good' and result [1] == 'good' and result[2] == 'good':
    likeDict['will like'] += (movie + ", ")
  elif result[0] == 'bad' and result [1] == 'bad' and result[2] == 'bad':
    likeDict['will not like'] += (movie + ", ")
  elif result[0] == 'good' and result [1] == 'good' and result[2] == 'bad':
    likeDict['will probably like'] += (movie + ", ")
  elif result[0] == 'bad' and result [1] == 'good' and result[2] == 'good':
    likeDict['will probably like'] += (movie + ", ")
  elif result[0] == 'good' and result [1] == 'bad' and result[2] == 'good':
    likeDict['will probably like'] += (movie + ", ")
  else:
    likeDict['will probably not like'] += (movie + ", ")

for x in likeDict: 
  if likeDict[x] != "":
    print("You", x, likeDict[x][0:-2])
    print()
print()
print()





#Uses the connections the code made in previous steps to test each of the parameters of each movies in the top 20 rated list and returns if the user will like/not like/probabaly like/probabaly not like based on the results.
likeDict = {
  "will like" : "",
  "will probably like" : "",
  "will probably not like" : "",
  "will not like" : ""
}

print("Using your likes and dislikes, out of the top 20 top rated movies in the entire movie database:")
print()
for i, movie in enumerate(mostpopular_titles):
  listFormat = [mostpopular_texts[i*3], mostpopular_texts[i*3+1], mostpopular_texts[i*3+2]]
  vectorFormat = vectorizer.transform(listFormat)
  result = classifier.predict(vectorFormat)
  if result[0] == 'good' and result [1] == 'good' and result[2] == 'good':
    likeDict['will like'] += (movie + ", ")
  elif result[0] == 'bad' and result [1] == 'bad' and result[2] == 'bad':
    likeDict['will not like'] += (movie + ", ")
  elif result[0] == 'good' and result [1] == 'good' and result[2] == 'bad':
    likeDict['will probably like'] += (movie + ", ")
  elif result[0] == 'bad' and result [1] == 'good' and result[2] == 'good':
    likeDict['will like'] += (movie + ", ")
  elif result[0] == 'good' and result [1] == 'bad' and result[2] == 'good':
    likeDict['will probably like'] += (movie + ", ")
  else:
    likeDict['will probably not like'] += (movie + ", ")

for x in likeDict: 
  if likeDict[x] != "":
    print("You", x, likeDict[x][0:-2])
    print()




#Looking at how the code makes its decisions visually is alot easier so I export the model to the tree.dot file. Upon copying all the data in tree.dot and pasting it in the textbox on http://www.webgraphviz.com/ you can see what the decision making process looks like.
tree.export_graphviz(
    classifier,
    out_file='tree.dot',
    feature_names=vectorizer.get_feature_names(),
    class_names=["bad","good"]

) 


