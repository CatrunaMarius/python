scoreList = []
markSheet =[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        markSheet  += [[name,score]]  
        scoreList += [score]
scoreList = list(dict.fromkeys(scoreList))
b=sorted(scoreList)[1]

for a,c in sorted(markSheet):
    if c == b:
        print(a)