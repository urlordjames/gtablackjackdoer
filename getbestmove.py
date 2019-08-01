import random
import numpy

def getmove(number, dealer=0):
    f = open("moves.csv", "r")
    chart = f.read().split(", ")
    f.close()
    chart = numpy.reshape(chart, [10, 10])
    number = playerscale(number)
    chardict = {
        "s": "stand",
        "h": "hit",
        "d": "double down",
    }
    if dealer == 0:
        print("no dealer value, picking random dealer value")
        return chardict[random.choice(chart[number])]
    else:
        dealer = dealerscale(dealer)
        return chardict[chart[number][dealer]]

def playerscale(number):
    numdict = {
        "20": 0,
        "19": 0,
        "18": 0,
        "17": 0,
        "16": 1,
        "15": 2,
        "14": 3,
        "13": 4,
        "12": 5,
        "11": 6,
        "10": 7,
        "9": 8,
        "8": 9,
        "7": 9,
        "6": 9,
        "5": 9,
        "4": 9,
        "1": 7,
        "2": 0
    }
    return numdict[str(number)]

def dealerscale(number):
    return number - 2
