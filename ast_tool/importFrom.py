import csv

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
