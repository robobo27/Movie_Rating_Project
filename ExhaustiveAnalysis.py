__author__ = 'Robert Arnold'

import datetime, Redo_Project_1v1
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
    for line in f:
        line = line.split(',')
        for r in range(len(line)):
            if r > 1: line[r] = float(line[r])
            if r == 1:
                line[r] = line[r].split('/')
                line[r] = datetime.date(int(line[r][2]),int(line[r][0]),int(line[r][1])).timetuple().tm_yday
        x.append(Movie(line))
    return x

def normalize(movie):
    #normalizes the data in the movie object
    v = movie.getDate()
    v1 = ((v -mins[0]))/(maxs[0] - mins[0])
    movie.setDate(v1)
    x = movie.getBudget()
    x1 = ((x -mins[1]))/(maxs[1] - mins[1])
    movie.setBudget(x1)
    # y = movie.getRating()
    # y1 = ((y -mins[2]))/(maxs[2] - mins[2])
    # movie.setRating(y1)
    z = movie.getRuntime()
    z1 = ((z -mins[3]))/(maxs[3] - mins[3])
    movie.setRuntime(z1)

def createMatrix(movieList,num):
    """
    :param movieList:
    :return: list of lists with just the movie data and no movie objects
    """
    z = []
    count = 0
    for s in movieList:
        y = []
        print(count,num)
        if count != num:
            for r in s:
                x = []
                # x.append(r.getRating())
                x.append(r.getDate())
                x.append(r.getBudget())
                x.append(r.getRuntime())
                y.append(x)
            z.append(y)
        if count == num:
            for r in s:
                q = []
                # q.append(r.getRating())
                q.append(r.getDate())
                q.append(r.getBudget())
                q.append(r.getRuntime())
        count += 1
    print(z)
    return z,q

def covariance(a):
    """
    returns a new covariance matrix, changed to be 2x2
    """
    p = Redo_Project_1
    meanA = p.mean(a)
    total = [[0,0],[0,0]]
    for r in range(len(a)):
        new = [[meanA[0]-a[r][0]],[meanA[1]-a[r][1]]]
        tnew = p.transpose(new)
        # print('tnew',tnew)
        mnew = p.multiply(new,tnew)
        # print('mnew',mnew)
        total = p.adds(total,mnew)
    return p.multiply(total,(1/len(a)))

def classer(Movies):
    """

    :param Movies:
    :return: list of three classified lists with movies sorted into respective ratings class
    """
    classes = [[] for r in range(3)]
    for r in Movies:
        x = int((r.getRating()-4)/2)
        # normalize(r)
        classes[x].append(r)
    return classes


def test(num):
    p = Redo_Project_1v1
    allMovies = reader('Movie_Data.csv')
    classes = classer(allMovies) # has normalized data and movie titles. Movies are classified correctly into 3 classes and retain movie objects
    matrix,testMovie = createMatrix(classes,num) # allows redo_project1 methods to work with the lists, leaves the test movie out of the data set
    print(len(classes))
    print(p.discriminant(matrix[0],matrix[1],matrix[2],testMovie))
    # for r in range(len(matrix)):
    #     print(p.mean(matrix[r]))
    # for s in range(len(matrix)): # finds misclassifications and prints them + the class sorted into and actual class
    #     print(s+1)
    #     for r in range(len(matrix[s])):
    #         x = p.discriminant(matrix[0],matrix[1],matrix[2],matrix[s][r])
    #         if(x) != "class "+str(s+1):
    #             print(classes[s][r],x,"class "+str(s+1))
    #     x = p.discriminant(matrix[0],matrix[1],matrix[2],p.mean(matrix[s]))
    #     print(p.mean(matrix[s]),x)


def main():
    for r in range(63):
        pass
test(0)