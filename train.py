import numpy as np
import pickle

def main():
    f = open("brown.txt", "r")  # assume that first char is a letter
    f = f.read()
    cur = ord(f[0].lower())-96 # cur is the index of the last letter in the array
    arr = np.zeros((28, 28))
    arr[0, cur] = 1
    last = True  # bool, whether or not last char was a letter
    for char in f[1:]:
        if not char.isalpha() and last is True:  # this means that a word was just completed
            arr[cur, 27] += 1  # then add to the cur -> end state
            last = False
        elif last is False and char.isalpha():  # if a word is starting
            cur = ord(char.lower())-96  # index of letter in arr
            arr[0, cur] += 1  # add to start -> cur state
            last = True  # last char was a letter
        elif char.isalpha():  # in the middle of a word
            arr[cur, ord(char.lower())-96] += 1  # add to last letter -> new letter state
            cur = ord(char.lower())-96  # change cur
            last = True
    if last:  # accounting for the last letter in the last word in the file, if that was a-z
        arr[cur, 27] += 1
    for i in range(28):  # turning all the values into probabilities
        val = sum(arr[i])  # take the sum of the row
        if val != 0:
            arr[i] /= val  # divide by the sum to turn each value into a probability

    f = open("arr.pkl", "wb")
    pickle.dump(arr, f)
    f.close()

main()
