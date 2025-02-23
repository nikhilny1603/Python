import pickle

f = open("text.txt","rb")
s = pickle.load(f)

print(s)