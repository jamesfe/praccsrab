import copy
import operator

def distroPoss(inStr, inDistTiles, blankTiles=2):
    '''Returns true/false if string is possible given distribution'''
    distTiles = copy.deepcopy(inDistTiles)
    for k in inStr.upper():
        distTiles[k] = distTiles[k]-1
        if(distTiles[k]<0): ## if there are no tiles left
            if(blankTiles>0): ## check to see if there is a blank one
                blankTiles-=1
            else:               ## if not available, not possible
                return(False)
    return(True)

def findQualifyingWords():
    '''
        Unsure what this function does. 
    '''
    ##tileDistro = dict({'A': 1, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4, 'V': 4, 'Y': 4, 'X': 8, 'Z': 10}) 
    tileDistro = dict({'A': 9, 'C': 2, 'B': 2, 'E': 12, 'D': 4, 'G': 3, 'F': 2, 'I': 9, 'H': 2, 'K': 1, 'J': 1, 'M': 2, 'L': 4, 'O': 8, 'N': 6, 'Q': 1, 'P': 2, 'S': 4, 'R': 6, 'U': 4, 'T': 6, 'W': 2, 'V': 2, 'Y': 2, 'X': 1, 'Z': 1})
    wordList = [a.strip() for a in file.read(file("../scrabble.txt", 'r')).split("\n")]
    qualifying = [[i, 0] for i in range(0, 4)]
    for k in range(0, len(wordList)):
        for qt in range(0, len(qualifying)):
            q = distroPoss(wordList[k], tileDistro, qualifying[qt][0])
            if(q==False):
                qualifying[qt][1] = qualifying[qt][1]+1
    print "Blank Tiles, Non-Qualifying Words"
    for k in qualifying:
        print k[0], k[1]

def genProbability(inStr, inDistTiles, blankTiles=0):
    ''' 
        Generate the probability that inStr can be created given 
        the distribution of inDistTiles with a default blank tile
        count of 0.
        inDistTiles is a dictionary of letters to ints.
    '''
    if(not distroPoss(inStr, inDistTiles, blankTiles)):
        #print inStr, "Not Possible"
        return(-1)
    inTiles = copy.deepcopy(inDistTiles)
    currProbability = float(1.0)
    for item in inStr.upper():
        totBag = sum(inTiles.values())+blankTiles
        probItem = float(inTiles[item])/float(totBag)
        inTiles[item] = inTiles[item]-1
        currProbability = currProbability * probItem
    return(currProbability)

def main():
    wordList = [a.strip() for a in file.read(file("../scrabble.txt", 'r')).split("\n")]
    tileDistro = dict({'A': 9, 'C': 2, 'B': 2, 'E': 12, 'D': 4, 'G': 3, 'F': 2, 'I': 9, 'H': 2, 'K': 1, 'J': 1, 'M': 2, 'L': 4, 'O': 8, 'N': 6, 'Q': 1, 'P': 2, 'S': 4, 'R': 6, 'U': 4, 'T': 6, 'W': 2, 'V': 2, 'Y': 2, 'X': 1, 'Z': 1})
    scores = []
    for k in wordList:
        if(len(k)>5):
            q = [k, genProbability(k, tileDistro)]
            if(q[1]>0):
                scores.append(q)
    scores = sorted(scores, key=operator.itemgetter(1), reverse=True)
    for k in scores[:100]:
        print k


if(__name__=="__main__"):
    main()
    ##findQualifyingWords()

