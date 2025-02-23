import pickle

example = {
    "Name" : "Nikhil",
    "Age": 20,
    "City ": "Ich"
}

pickle_write = open("text.txt","wb")
pickle.dump(example, pickle_write)
pickle_write.close()

