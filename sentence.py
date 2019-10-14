import pickle
import numpy as np

def main():
    f = open("words_sentences.pkl", 'rb')
    sents = pickle.load(f)
    arr = {}

    for sent in sents:
        curVal = sent[0].lower()
        if curVal in arr:
            if curVal in arr['START']:
                arr['START'][curVal] += 1
            else:
                arr['START'][curVal] = 1
        else:
            arr['START'] = {}
            arr['START'][curVal] = 1
        for w in sent[1:]:
            word = w.lower()
            if curVal in arr:
                if word in arr[curVal]:
                    arr[curVal][word] += 1
                else:
                    arr[curVal][word] = 1
            else:
                arr[curVal] = {}
                arr[curVal][word] = 1
            curVal = word
        if curVal in arr:
            if 'END' in arr[curVal]:
                arr[curVal]['END'] += 1
            else:
                arr[curVal]['END'] = 1
        else:
            arr[curVal] = {}
            arr[curVal]['END'] = 1

    for k in arr:
        sum = 0
        for k1, v1 in arr[k].items():
            sum += v1
        for k1, v1 in arr[k].items():
            arr[k][k1] /= sum

    print(simulate(arr))

def simulate(tMat1):
    string = ''
    tMat = tMat1.copy()
    for k in tMat:
        sum = 0
        for k1, v1 in tMat[k].items():
            tMat[k][k1] += sum
            sum = tMat[k][k1]

    rand = np.random.random()
    for k, v in tMat['START'].items():
        if rand < v:
            string += k
            string += " "
            curState = k
            break

    while True:
        rand = np.random.random()
        for k, v in tMat[curState].items():
            if rand < v:
                curState = k
                break
        if curState != 'END':
            if curState == "." or curState == "," or curState == ";" or curState == ":" or curState == "?" or curState == "!":
                string = string[:-1]
            string += curState
            string += " "
        else:
            break
    return string


main()
