# Should put all of the imports at the top of the file
import random
import csv
import matplotlib.pyplot as plt


# The coursework specification required a function named game -
# don't change this (e.g. to squashgame(a, b))
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


# Note the use of a default value for the simulations -
# this lets the calling code override this value if
# needed. In general, avoid having hard coded values
# inside your functions.
def winProbability(arank, brank, simulations=10000):
    awins = 0
    # This should definitely be a for loop (as we know
    # we need a fixed number of iterations). Note that
    # range(simulations) is equivalent and preferable to
    # range(0, simulations) or range(1, simulations+1)
    for i in range(simulations):
        (a, b), r = game(arank, brank)
        if a > b:
            awins += 1
        # Lots of answers also counted the number of wins for b,
        # this is fine, but redundant as the value is not needed.

    # A lot of answers rounded this value before returning
    # it. It's better to  return the most accurate answer
    # and let the code that calls the function handle rounding.
    # Also, use the built in round function rather than writing
    # your own (and converting to a string and back is error
    # prone and inelegant)
    return awins / simulations


def englishgame(arank, brank):
    pa = arank / (arank + brank)
    pb = brank / (arank + brank)

    players = ['a', 'b']
    eight = ''

    server = random.choice(players)

    scores = {'a': 0, 'b': 0}
    rallies = 0

    aim = 9
    decisionMade = False

    while max(scores.values()) < aim:
        # If 8-8 for the first time, decide final score
        if (max(scores.values()) == 8 and min(scores.values()) == 8):
            if not decisionMade:
                decisionMade = True
                # Assume players are rational - weaker players would
                # rather play one point and get lucky. This scored more
                # marks than selecting randomly or always chosing either
                # 9 or 10
                if pa < pb and eight == 'a' or pb < pa and eight == 'b':
                    aim = 9
                else:
                    aim = 10

        if random.random() < pa:
            winner = 'a'
        else:
            winner = 'b'
        rallies += 1
        # Avoid repeating code where possible, many answers had:
        # if random.random() < pa:
        #     rallies += 1
        #     winner = 'a'
        # else:
        #     rallies += 1
        #     winner = 'b'

        if winner == server:
            scores[server] += 1
            # store the first to eight in case of draw
            if scores[server] == 8 and eight not in players:
                eight = server
        else:
            server = list(set(players) - set([server]))[0]

    return (scores['a'], scores['b']), rallies


# One neat feature of Python is that you can pass functions as
# arguments - this lets us make this function handle both
# PARS & English
def match(arank, brank, n, gamefunc=game):
    ascore = 0
    bscore = 0
    rallies = 0

    while max(ascore, bscore) < n:
        (a, b), r = gamefunc(arank, brank)
        rallies += r
        if a > b:
            # Avoid redundant comments, e.g.
            # Add one to ascore
            # is clear from the code itself
            ascore += 1
        else:
            bscore += 1

    return (ascore, bscore), rallies


def matchWinProbability(arank, brank, n, simulations=10000, gamefunc=game):
    awins = 0
    for i in range(simulations):
        (a, b), r = match(arank, brank, n, gamefunc)
        if a > b:
            awins += 1
        # Some answers calculated the probability on every iteration
        # prob = awins / simulations
        # This is inefficient as the intermediate values are never
        # used.
    return awins / simulations


def readCSV(filename):
    with open(filename) as csvfile:
        # Quite a few people used poor variable names here - e.g.
        # l is easily confused with 1 and list is already a keyword
        # in Python
        data = []
        reader = csv.reader(csvfile)
        # Should add a comment to say why next is called
        # Skip the file header
        next(reader, None)
        for row in reader:
            # The type of the ranking wasn't specified
            # float is a little neater than int
            data.append((float(row[0]), float(row[1])))
            # Note that it's more efficient to skip the first row
            # rather than using a variable and checking on every
            # iteration:
            # if not firstLine:
            #    data.append((float(row[0]), float(row[1])))
    return data


def plotWinProbabilities(data):
    x = []
    y = []
    for (ra, rb) in data:
        x.append(ra / rb)
        y.append(winProbability(ra, rb))
        # So many answers plotted the probability of winning
        # a point rather than a game:
        # y.append(ra / (ra + rb))
        # that I decided the wording must have been unclear
        # and gave everyone full marks for the functionality
        # part of this question
    # Could also create these lists in a more concise way
    # x = [ra / rb for ra, rb in data]
    # y = [winProbability(ra, rb) for ra, rb in data]
    plt.plot(x, y, 'o')
    # I've chosen to plot with just circles at the data points -
    # if you want to plot a line between them, you need to sort the
    # points first, e.g. add the line:
    # data = sorted(data, key=lambda x: x[0] / x[1])
    # at the start of this function
    # Note that you can't just sort x and y independently -
    # you'll  lose the link between the two values at each
    # data point
    plt.xlabel("ra/rb")
    plt.ylabel("Probability a wins")
    # I've hardcoded the filename - it would be neater to pass as
    # an argument e.g. plotWinProbabilities(data, filename="test.pdf")
    # and plt.savefig(filename)
    plt.savefig("test.pdf")
    plt.show()


def rallies(arank, brank, n, gamefunc, simulations):
    rallies = 0
    best_wins = 0
    # You'll often see _ used as the loop variable, to
    # indicate that the value isn't used inside the loop
    for _ in range(simulations):
        (a, b), r = match(arank, brank, n, gamefunc)
        rallies += r
        if a > b and arank > brank or a < b and arank < brank:
            best_wins += 1
    return rallies / simulations, best_wins / simulations


def q1a():
    random.seed(57)
    print(game(70, 30))


def q1b():
    random.seed(57)
    print(round(winProbability(70, 30), 2))


def q1c():
    print(readCSV('test.csv'))


def q1d():
    plotWinProbabilities(readCSV('test.csv'))


def q1e():
    n = 1
    while matchWinProbability(60, 40, n) < 0.9:
        n += 1
    print(n)


# Main finding should be that English scoring is more likely to result
# in the correct winner, however at the expense of much longer matches.
# This effect is increased as the number of games in a match increases.
# Answer should include a figure that allows the easy comparison of these
# two measures (see attached). Assumptions could include aspects such as:
#    - Players are equally good when serving/receiving
#    - Players are equally fit
#    - All rallies take the same (average) time
def q2():
    # Note that I build the input data programmatically, rather than
    # typing in lots of values by hand. Try to minimise the number of
    # literal values you have in your code
    aranks = list(range(1, 201, 1))
    brank = 50
    x = [arank / brank for arank in aranks]
    # A common mistake was to use too few simulations - this results
    # in a jagged graph. I've used quite a lot of data points here -
    # this will take about 5 minutes to run, but gives a nice, smooth
    # output.
    simulations = 5000

    fig, (rally_ax, win_ax) = plt.subplots(2)

    # Question 2 asks about "matches" not "games" - I also wanted to
    # see how the number of games in a match affects things
    for n in range(1, 4):
        pars_rallies = []
        english_rallies = []
        pars_wins = []
        english_wins = []
        for arank in aranks:
            print(arank)
            rally_prop, wins = rallies(arank, brank, n, game, simulations)
            pars_rallies.append(rally_prop)
            pars_wins.append(wins)

            rally_prop, wins = rallies(arank, brank, n, englishgame, simulations)
            english_rallies.append(rally_prop)
            english_wins.append(wins)
        rally_ax.plot(x, pars_rallies, '-', label=str(n) + " pars")
        rally_ax.plot(x, english_rallies, '--', label=str(n) + " english")
        win_ax.plot(x, pars_wins, '-', label=str(n) + " pars")
        win_ax.plot(x, english_wins, '--', label=str(n) + " english")
    rally_ax.set_xlabel('ra/rb')
    rally_ax.set_ylabel('Number of rallies')
    win_ax.set_xlabel('ra/rb')
    win_ax.set_ylabel('Probability best wins')
    rally_ax.legend()
    plt.show()


# q1a()
# q1b()
# q1c()
# q1d()
# q1e()
# q2()
