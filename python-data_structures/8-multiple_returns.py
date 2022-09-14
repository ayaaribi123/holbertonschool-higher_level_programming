#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        return (len(sentence), None)
    mul = (len(sentence), sentence[0])
    return mul
