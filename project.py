from numpy import *
import operator
from os import listdir
#function for calculating and returning best match class
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
         voteIlabel = labels[sortedDistIndicies[i]]
         classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
         sortedClassCount = sorted(classCount.iteritems(),
         key=operator.itemgetter(1), reverse=True)      
    return sortedClassCount[0][0]

#primitive function to create a dataset and corresponding label set
def createDataSet():
         group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
         labels = ['A','A','B','B']
         return group, labels
#function to parse text file and find dataset and label set
def file2matrix(filename):
        fr = open(filename)
        numberOfLines = len(fr.readlines())         #get the number of lines in the file
        returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector


#function for normalizing dataset matrix
def autoNorm(dataSet):
        minVals = dataSet.min(0)
        maxVals = dataSet.max(0)
        ranges = maxVals - minVals
        normDataSet = zeros(shape(dataSet))
        m = dataSet.shape[0]
        normDataSet = dataSet - tile(minVals, (m,1))
        normDataSet = normDataSet/tile(ranges, (m,1))   
#element wise divide
    return normDataSet, ranges, minVals
   #complete classification function 
def ClassTest():
        #hold out 10%
        hoRatio = 0.50      
       #load dataset from file
        DataMat,DataLabels = file2matrix('TestSet.txt')
        normMat, ranges, minVals = autoNorm(DataMat)
        m = normMat.shape[0]
        numTestVecs = int(m*hoRatio)
        errorCount = 0.0
        for i in range(numTestVecs)
               classifierResult=classify0(normMat[i,:],

               normMat[numTestVecs:m,:],
               DataLabels[numTestVecs:m],3)
               print "the classifier came back with: %d, the real answer is:
              %d" % (classifierResult, datingLabels[i])                   
              if (classifierResult != DataLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))
    print errorCount
    
#function to test the classifier
def classifyPerson():
	resultList = ['not at all','in small doses', 'in large doses']
	percentTats = float(raw_input(\
	"percentage of time spent playing video games?"))
	ffMiles = float(raw_input("frequent flier miles earned per year?"))
	iceCream = float(raw_input("liters of ice cream consumed per
          year?"))
	DataMat, DataLabels = file2matrix('TestSet.txt')
	normMat, ranges, minVals = autoNorm(DataMat)
	inArr = array([ffMiles, percentTats, iceCream])
	classifierResult = classify0((inArr-\
	minVals)/ranges,normMat,DataLabels,3)
	print "You will probably like this person: ",\
	resultList[classifierResult - 1]
