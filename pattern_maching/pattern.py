import re

#####
# 宣告要比對的兩個檔案名稱
# 以及要比對的pattern
#####
filenameA = 'a.php'
filenameB = 'b.php'
MatchingPattern = '(\'[a-z_]*\')'


fileA = open(filenameA,'r',encoding = 'utf8')
contentA = fileA.read();
patternA=re.findall(MatchingPattern,contentA)

fileB = open(filenameB,'r',encoding = 'utf8')
contentB = fileB.read();
patternB=re.findall(MatchingPattern,contentB)

# result area
resultIntersect = list(set(patternA).intersection(set(patternB))) #交集
resultUnion = list(set(patternA).union(set(patternB))) ##並集
##resultDiff = list(set(patternA).difference(set(patternB))) ##差集
resultDiff2 = list(set(resultUnion).difference(set(resultIntersect))) ## 並集-交集

print(resultDiff2)
