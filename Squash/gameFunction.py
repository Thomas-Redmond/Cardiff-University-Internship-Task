import random


def game(arank, brank):
    # If you name the variables well, they don't need any additional comments
    pa = arank / (arank + brank)

    ascore = 0
    bscore = 0

    # There are lots of different ways of writing the loop. Some answers
    # used two loops (one to get to 11 points, and then one to get the
    # two clear points) - this isn't as elegant as a single condition.
    while (max(ascore, bscore) < 11 or
           max(ascore, bscore) - min(ascore, bscore) < 2):
        if random.random() < pa:
            ascore += 1
        else:
            bscore += 1

    # There were a few variations on this loop, for example:
    # while True:
    #     if (max(ascore, bscore) >= 11:
    #        if max(ascore, bscore) - min(ascore, bscore) >= 2):
    #           break
    #     if random.random() < pa:
    #         ascore += 1
    #     else:
    #         bscore += 1
    # This is functionally the same, but harder to read - it's
    # clearer if the reader can tell from the first line of the
    # loop when it will end. Another similar and common style was:
    # status = True
    # while status:
    #     if (max(ascore, bscore) >= 11:
    #        if max(ascore, bscore) - min(ascore, bscore) >= 2):
    #           return ascore, bscore
    #           status = False
    #     if random.random() < pa:
    #         ascore += 1
    #     else:
    #         bscore += 1
    # Note that the use of status is redundant - the only line
    # modifying the variable can't be reached, as the line before
    # returns from the function. Similarly:
    #           status = False
    #           return ascore, bscore
    # is equally untidy - the new value of status is never used

    # Note the function returns the number of rallies too, so
    # that the function can be used with Question 2.
    # For PARS scoring, the number of rallies is equal to the
    # sum of the points (since every rally results in a point).
    # For an answer just for question 1a, the line could be
    # replaced by
    # return (ascore, bscore)
    return (ascore, bscore), ascore + bscore
