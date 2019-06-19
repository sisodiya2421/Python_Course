import numpy as np

def createTable(inp, k=3):
    T={}
    for i in range(len(inp)-k):
        X = inp[i:i+k]
        Y = inp[i+k]
        if X in T:
            if Y in T[X]:
                T[X][Y] += 1
            else:
                T[X][Y] = 1
        else:
            T[X] = {
                Y: 1
            }
    return T

def convertToProbability(model):
    for X in model:
        s= sum(model[X].values())
        for Y in model[X]:
            model[X][Y] /= s
    return model

def sampleNext(inp, model):
    inp = inp[-3]
    if inp in model:
        outcomes = list(model[inp].keys())
        prob = list(model[inp].values())
        return np.random.choice(outcomes, p = prob)
    else:
        return ' '


def generateText(start, model, length=1000):
    for _ in range(length):
        start += sampleNext(start, model)
    return start
    
def getThingsDone():
    lyr=input("Enter The lyrics of any song ")
    word = input("Enter the word ")
    #print(type(lyrics))
    #print(type(word))  
    model = convertToProbability(createTable(lyr))
    generatedWord = generateText(word,model)
    return generatedWord

print(getThingsDone())
