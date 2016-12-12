__author__ = 'Robert Arnold'
import math
import random
def adds(a, b):
    """
    Adds 2 matrices together, given that they have the same dimensions
    and returns one matrix of the sum
    """
    m = []
    if type(a[0]) != list:
        for s in range(len(b)):
            m.append(a[s]+b[s])
        return m
    if len(a[0]) != len(b[0]) or len(a) != len(b):
        raise KeyError("Sizes do not match")
    for r in range(len(a)):
        new = []
        for s in range(len(a[0])):
            new.append(a[r][s] + b[r][s])
            #print(new)
        m.append(new)
        #print(m)
    return m

def sub(a,b):
    """
    subtracts two matrices ogf the same size
    :param a:
    :param b:
    :return:
    """
    b = multiply(b,-1)
    return adds(a,b)

def multiply(a,b):
    """
    performs scalar multiplication, vector and matrix multiplication
    :param a:
    :param b:
    :return multiplied matrix:
    """
    m = []
    if type(a) != list or type(b) != list:
        #For scalar multiplication of a matrix
        if type(a) != list:
            new = []
            for r in range(len(b)):
                if type(b[0]) != list:
                    m.append(a*b[r])
                else:
                    m = []
                    for s in range(len(b[0])):
                        m.append(a*b[r][s])
                    new.append(m)
            if type(b[0]) != list:
                new.append(m)
            if len(new) == 1:
                return new[0]
            else:
                return new
        if type(b) != list:
            new = []
            for r in range(len(a)):
                if type(a[0]) != list:
                    m.append(b*a[r])
                else:
                    m = []
                    for s in range(len(a[0])):
                        m.append(b*a[r][s])
                    new.append(m)
            if type(a[0]) != list:
                new.append(m)
            if len(new) == 1:
                return new[0]
            else:
                return new
    else:
        #for matrix multiplied by a matrix
        if type(a[0]) != list:
            #for a = 1xn and b = nxn
            if len(a) != len(b):
                raise KeyError("Sizes do not match")
            else:
                new = []
                for r in range(len(b[0])):
                    m = []
                    for s in range(len(b)):
                        # for q in range(len(a)):
                        m.append(a[s]*b[s][r])
                        # print('m',m)
                    # if len(b[0]) == 1:
                    # print('made it')
                    new.append(sum(m))
                        # else:
                        #     new.append(m)
                        #     print('new',new)
                return new
        elif type(b[0]) != list:
            #for a = nx1 and b = 1xn
            if len(a) != len(b):
                raise KeyError("Sizes do not match")
            else:
                new = []
                for r in range(len(a)):
                    m = []
                    for s in range(len(a)):
                        m.append(b[s]*a[r][0])
                    new.append(m)
                return new


        else:
            if len(a[0]) != len(b):
                #for a = nxn and b = nxn
                raise KeyError("Sizes do not match")
            else:
                ret = []
                for r in range(len(a)):
                    for s in range(len(a[0])):
                        new = []
                        for q in range(len(b[0])):
                            m = []
                            for p in range(len(b)):
                                m.append(a[r][p]*b[p][q])
                            new.append(sum(m))
                    ret.append(new)
                return ret

def mean(a):
    """
    :param a:
    :return mean of the given vector :
    """
    m = []
    # if type(a[0]) == list:
    for r in range(len(a[0])):
        new = 0
        for s in range(len(a)):
            new += a[s][r]
        m.append(new/len(a))
    return m


def covariance(a):
    """
    returns a new covariance matrix, changed to be 3x3
    """
    meanA = mean(a)
    total = [[0,0,0],[0,0,0],[0,0,0]]
    for r in range(len(a)):
        new = [[meanA[0]-a[r][0]],[meanA[1]-a[r][1]],[meanA[2] - a[r][2]]]
        tnew = transpose(new)
        # print('tnew',tnew)
        mnew = multiply(new,tnew)
        # print('mnew',mnew)
        total = adds(total,mnew)
    return multiply(total,(1/len(a)))

def swap(a,b):
    #returns the two items reverse of their input
    return b, a

def GaussJordan(c):
    """

    :param matrix c:
    :return reduced matrix by process of Gauss-Jordan elimination:
    """
    p = 0
    E = 1
    for j in range(len(c)):
        #print(c)
        for i in range(j,len(c)):
            if abs(c[i][j]) > abs(c[p][j]):
                p = i
                #print(p)
        if c[p][j] == 0:
            E = 0
            return E
        if p > j:
            c[p], c[j] = swap(c[p],c[j])
        # print(c[j][j])
        c[j] = multiply(c[j],1/c[j][j])

        for ir in range(len(c)):#for the rows
            if ir != j:
                #print('1st C',c)
                subtractor = multiply(c[ir][j],c[j])
                #print('sub',subtractor)
                for ic in range(len(c[0])):#for the columns
                    #print('c[ir][ic]',c[ir][ic])
                    c[ir][ic] = c[ir][ic] - subtractor[ic]
                    #print('new c[ir][ic]',c[ir][ic])
                #print('C',c)
    return c


def determinant(c):
    """

    :param matrix c:
    :return reduced matrix by process of Gaussian elimination:
    """
    p = 0
    r = 0
    for j in range(len(c)):
        #print(c)
        for i in range(j,len(c)):
            if abs(c[i][j]) > abs(c[p][j]):
                p = i
        #print('p',p,'j',j)
        if c[p][j] == 0:
            delta = 0
            return delta
        if p > j:
            c[p], c[j] = swap(c[p],c[j])
            r += 1


        for ir in range(len(c)):#for the rows
            if ir > j:
                #print('1st C',c)
                subtractor = multiply((c[ir][j]/c[j][j]),c[j])
                for ic in range(len(c[0])):#for the columns
                    #print('c[ir][ic]',c[ir][ic])
                    c[ir][ic] = c[ir][ic] - subtractor[ic]
    delta = 1
    for j in range(len(c)):
        delta = delta * c[j][j]
        #print(delta)

    return ((-1)**r)*delta

def inverse(c):
    """
    Uses GaussJoradan elimination in order to determine the inverse of the
    matrix c
    :param c:
    :return:
    """
    for j in range(len(c)):
        for i in range(len(c[j])):
            if i == j:
                c[j].append(1)
            else:
                c[j].append(i-i)
    # print(c)
    c = GaussJordan(c)
    for j in range(len(c)):
        c[j] = c[j][len(c[j])//2:len(c[j])]

    return c

def identity(n,m):
    """
    takes the size of desired matrix and return an identity matrix with that dimension
    :param n:
    :param m:
    :return:
    """
    q = []
    for j in range(n):
        new = []
        for i in range(m):
            if i == j:
                new.append(1)
            else:
                new.append(i-i)
        q.append(new)
    return q

def transpose(a):
    """
    :param a:
    :return the transposed matrix of a:
    """
    new = []
    result = []
    if type(a[0]) != list:
        for r in range(len(a)):
            new.append([a[r]])
        return new
    else:#if type(a[0][0]) != list:
        for r in range(len(a[0])):
            new = []
            for s in range(len(a)):
                if len(a[0]) > 1:
                    if type(a[0][0]) != list:
                        new.append(a[s][r])
                    else:
                        for t in range(len(a[s][r])):
                            new.append(a[s][r][t])
                else:
                    result.append(a[s][r])
            if len(new) != 0:
                result.append(new)
        return result

def data(filename):
    """
    creates two classes of data from the given file as 2xn matrices
    :return:
    """
    dataSet1 = []
    dataSet2 = []
    with open(filename) as f:
    # with open('2015 Test 1 data.txt') as f:
        f.readline()
        for line in f:
            line = line.strip()
            line = line.split('\t')
            dataSet1.append([float(line[0]),float(line[1])])
            # dataSet2.append([float(line[2]),float(line[3])])
    return dataSet1  #dataSet2

def g1(class1, vector):
    """
    returns the discriminant for a given class and vector
    """
    #class 1 data
    class1mean = mean(class1)
    class1covariance = covariance(class1)
    class1inverse = inverse(class1covariance)
    class1covariance = covariance(class1)
    class1determinant = determinant(class1covariance)
    g1m = .5*math.log(class1determinant)

    #class 1 function
    v1 = [vector[0] - class1mean[0], vector[1] - class1mean[1]]
    v1trans = transpose(v1)
    v2 = multiply(v1,class1inverse)
    g1vector = multiply(v2,v1trans)
    rest1 = -.5*(g1vector[0]) - g1m

    return rest1


def discriminant(class1,class2,class3,vector):
    """
    determines if a given vector is in class1 or class2 # adjusted for 3 classes
    :param class1:
    :param class2:
    :param class3:
    :param vector:
    :return string class1 or class 2 or class 3:
    """
    length = len(class1)+len(class2)+len(class3)

    #class 1 data
    class1mean = mean(class1)
    class1covariance = covariance(class1)
    class1inverse = inverse(class1covariance)
    class1covariance = covariance(class1)
    class1determinant = determinant(class1covariance)
    g1m = .5*math.log(class1determinant)

    #class 2 data
    class2mean = mean(class2)
    class2covariance = covariance(class2)
    class2inverse = inverse(class2covariance)
    class2covariance = covariance(class2)
    class2determinant = determinant(class2covariance)
    g2m = .5*math.log(class2determinant)

    #class 3 data
    class3mean = mean(class3)
    class3covariance = covariance(class3)
    # print(class3covariance)
    class3inverse = inverse(class3covariance)
    class3covariance = covariance(class3)
    class3determinant = determinant(class3covariance)
    # print(class3determinant)
    g3m = .5*math.log(class3determinant)

    #class 1 function
    v1 = [vector[0] - class1mean[0], vector[1] - class1mean[1], vector[2] - class1mean[2]]
    v1trans = transpose(v1)
    v2 = multiply(v1,class1inverse)
    g1vector = multiply(v2,v1trans)
    rest1 = -.5*(g1vector[0]) - g1m + math.log(len(class1)/length)

    #class 2 function
    v1 = [vector[0] - class2mean[0], vector[1] - class2mean[1], vector[2] - class2mean[2]]
    v1trans = transpose(v1)
    v2 = multiply(v1,class2inverse)
    g1vector = multiply(v2,v1trans)
    rest2 = -.5*(g1vector[0]) - g2m + math.log(len(class2)/length)

    #class 3 function
    v1 = [vector[0] - class3mean[0], vector[1] - class3mean[1], vector[2] - class3mean[2]]
    v1trans = transpose(v1)
    v2 = multiply(v1,class3inverse)
    g1vector = multiply(v2,v1trans)
    rest3 = -.5*(g1vector[0]) - g3m + math.log(len(class3)/length)

    m = max(rest1,rest2,rest3)
    if m == rest1:
        return 'class 1'
    elif m == rest2:
        return 'class 2'
    else:
        return 'class 3'


def boundary(m1,m2):
    """
    boundary for project 1
    """
    minx = -7
    miny = -7
    maxx = 7
    maxy = 12
    epsilon = .5
    new  = []
    for x in range(minx,maxx,1):
        for y in range(miny,maxy,1):
            if abs(g1(m1,[x,y]) - g1(m2,[x,y])) < epsilon:
                new.append([x,y])
    return new

def norm(c):
    """
    :param c:
    :return: norm of the given matrix
    """
    max1 = 0
    for j in range(len(c)):
        summ = 0
        if type(c[0]) == list:
            for i in range(len(c[0])):
                summ += abs(c[j][i])
        else:
            summ += abs(c[j])
        if summ > max1:
            max1 = summ
    return max1

def condition(c):
    """
    returns condition of a matrix
    """
    max1 = norm(c)
    max2 = norm(inverse(c))
    return max1*max2

def trace(c):
    """
    finds the trace of a given matrix
    :param c:
    :return:
    """
    sum = 0
    for i in range(len(c)):
        for j in range(len(c[i])):
            if i == j:
                sum += c[i][j]
    return sum

def leverrier(a):
    """
    for nxn matrices
    :param a:
    :return: coefficients in descending order of charachteristic polynomial
    """
    coeff = []
    B = a
    coeff.append(0-trace(B))
    k = len(B)-1
    while k != 0:
        B = adds(B,multiply(coeff[-1],identity(len(B),len(B[0]))))
        # print('b',B)
        B = multiply(a,B)
        coeff.append(0-trace(B)/(len(a)-k+1))
        k -= 1
    return coeff

def distance(a,b):
    """
    returns the distance between the two points given by 2 lists or tuples
    :param a point 1[x,y]:
    :param b point 2[x,y]:
    :return:
    """

    n = (float(b[0]) - float(a[0]))**2 + (float(b[1]) - float(a[1]))**2
    d = math.sqrt(n)
    return d

def quadratic(a):
    """
    solves a polynomial with a power of 2
    :param a:
    :return:
    """
    posx = (- a[1] + math.sqrt(a[1]**2 -4*a[0]*a[2]))/(2*a[0])
    negx = (- a[1] - math.sqrt(a[1]**2 -4*a[0]*a[2]))/(2*a[0])
    return [posx, negx]


def companion(c):
    """

    :param c:
    :return: companion matrix for the given polynomial starting at a0 going to an-1
    """
    q = []
    x = []
    for r in range((len(c))):
        x.append(-c[r])
    q.append(x)
    for i in range(len(c)-1):
        x = []
        for j in range(len(c)):
            if i  == j:
                x.append(1)
            else:
                x.append(0)
        q.append(x)
    return q

def power(c):
    """
    runs the given matrix through the power algorithm and return the largest eiganvalue and its vector
    :param c:
    :return:
    """
    epsilon = .000001
    m = 100
    k = 0
    y = []
    r = [[10, 10, 10], [10, 10, 10]]
    A = c
    print(A)
    while len(y) < len(c):
        y.append([random.random() - .5])
    x = multiply(A, y)
    print('k', '\t''\t', 'u', '\t''\t', 'y', '\t''\t', 'r')
    while (norm(r) > epsilon and k < m):
        y = multiply(x, 1 / norm(x))
        x = multiply(A, y)
        transy = transpose(y)
        num = multiply(transy, x)
        den = multiply(transy, y)
        u = num[0] / den[0]
        r = sub(multiply(y, u), x)
        print(k, '\t', u, '\t', y, '\t', norm(r))
        k += 1


def main():
    m1 = data('S2016 P1 data.txt')
    print(covariance(m1))
    # print(mean(m1))
    # print(mean(m2))
    # print(g1(m2,mean(m1)))
    # print(covariance(m2))
    # print(determinant(covariance(m2)))
    # print(inverse(covariance(m2)))
    # for r in m1:
    #     if(discriminant(m1,m2,r)) != "class 1":
    #         print(r)
    dataset = [[2,3,8,2,0,1,4,-3,5],[-14,3,1,2,-1,1,2,1,4],[2,13,2,2,3,-4,2,1,11],
              [1,7,0,8,-1,6,-1,1,2],[3,-2,2,3,0,2,3,4,21],[1,1,2,2,1,2,-3,5,1],
              [-9,0,3,1,-3,-1,0,-2,12],[2,-1,0,0,3,0,1,-3,22]]
    # dataset = [[2,3,8,2,0,1,4,-3],[-14,3,1,2,-1,1,2,1],[2,13,2,2,3,-4,2,1],
    #           [1,7,0,8,-1,6,-1,1],[3,-2,2,3,0,2,3,4],[1,1,2,2,1,2,-3,5],
    #           [-9,0,3,1,-3,-1,0,-2],[2,-1,0,0,3,0,1,-3]]
    # print(determinant(dataset))
    # print(inverse(dataset))
    # print(GaussJordan(dataset))
    # x = [[100,-200],[-200,401]]
    x = [[4,-6,9],[5,8,-2],[7,-3,1]]
    # print(condition(x))
    # print(determinant(dataset))
    # print(determinant(x))
if __name__ == '__main__':
    main()
