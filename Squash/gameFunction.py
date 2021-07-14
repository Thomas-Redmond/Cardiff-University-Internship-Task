import random


def game(arank, brank):
    pa = arank / (arank + brank)

    ascore = 0
    bscore = 0

    while (max(ascore, bscore) < 11 or
           max(ascore, bscore) - min(ascore, bscore) < 2):
        if random.random() < pa:
            ascore += 1
        else:
            bscore += 1

    return (ascore, bscore), ascore + bscore
