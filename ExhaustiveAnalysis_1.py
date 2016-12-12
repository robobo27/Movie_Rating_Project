__author__ = 'Robert Arnold'

import datetime, Redo_Project_1
maxs = [359,225000000,8.9,195]
mins = [6,2700000,4.8,69]

class Movie:
    #takes a 5 item list and creates a new Movie object
    Title = None
    Date = None
    Budget = None
    Rating = None
    Runtime = None

    def __init__(self,line):
        self.Title = line[0]
        self.Date = line[1]
        self.Budget = line[2]
        self.Rating = line[3]
        self.Runtime = line[4]

    def __str__(self):
        # return self.Title + '\n' + str(self.Date) + '\n' + str(self.Budget) + '\n' + str(self.Rating) + '\n' + str(self.Runtime)
        return self.Title + ',' + str(self.Date) + ',' + str(self.Budget) + ',' + str(self.Rating) + ',' + str(self.Runtime)
    def getTitle(self):
        return self.Title

    def getDate(self):
        return self.Date

    def getBudget(self):
        return self.Budget

    def getRating(self):
        return self.Rating

    def getRuntime(self):
        return self.Runtime

    def setTitle(self, new):
        self.Title = new

    def setDate(self, new):
        self.Date = new

    def setBudget(self, new):
        self.Budget = new

    def setRating(self, new):
        self.Rating = new

    def setRuntime(self, new):
        self.Runtime = new

def reader(file):
    x = []
    f = open(file)
    f.readline()
    max = 0
    min = 100
    for line in f:
        line = line.split(',')
        for r in range(len(line)):
            if r > 1: line[r] = float(line[r])
            if r == 1:
                line[r] = line[r].split('/')
                line[r] = datetime.date(int(line[r][2]),int(line[r][0]),int(line[r][1])).timetuple().tm_yday
                if line[r] > max: max = line[r]
                if line[r] < min: min = line[r]
        x.append(Movie(line))
    return x

def normalize(movie):
    #normalizes the data in the movie object
    v = movie.getDate()
    v1 = ((v -mins[0])*1)/(maxs[0] - mins[0])
    movie.setDate(v1)
    x = movie.getBudget()
    x1 = ((x -mins[1])*1)/(maxs[1] - mins[1])
    movie.setBudget(x1)
    # y = movie.getRating()
    # y1 = ((y -mins[2])*1)/(maxs[2] - mins[2])
    # movie.setRating(y1)
    z = movie.getRuntime()
    z1 = ((z -mins[3])*1)/(maxs[3] - mins[3])
    movie.setRuntime(z1)

def createMatrix(movieList):
    y = []
    for r in movieList:
        x = []
        x.append(r.getDate())
        x.append(r.getBudget())
        x.append(r.getRuntime())
        y.append(x)
    return y

def covariance(a):
    """
    returns a new covariance matrix, changed to be 3x3
    """
    p = Redo_Project_1
    meanA = p.mean(a)
    total = [[0,0,0],[0,0,0],[0,0,0]]
    for r in range(len(a)):
        new = [[meanA[0]-a[r][0]],[meanA[1]-a[r][1]],[meanA[2] - a[r][2]]]
        tnew = p.transpose(new)
        # print('tnew',tnew)
        mnew = p.multiply(new,tnew)
        # print('mnew',mnew)
        total = p.adds(total,mnew)
    return p.multiply(total,(1/len(a)))



def test():
    p = Redo_Project_1
    allMovies = reader('Movie_Data.csv')
    classes = [[] for r in range(5)]
    movieMatrix = createMatrix(allMovies)
    for r in allMovies:
        classes[int((r.getRating()-4)/1.2)].append(r)
    print(covariance(createMatrix(classes[0])))
    # for r in classes:
    #     x = 0
    #     count = 0
    #     print('star')
    #     for s in r:
    #         print(s.getTitle())#,s.getBudget())
    #         x += s.getBudget()
    #         count += 1
        # print(x/count)

    # print(movieMatrix)
    # print(p.mean(movieMatrix))
    # print(covariance(movieMatrix))
    # print(mean)
    # print(mov.getBudget())
    # print(mov.getRating())
    # print(mov.getRuntime())


test()