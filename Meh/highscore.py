scores=input('Enter the scores: ').split()
high_score=0
score=0
for n in range(0,len(scores)):
    score=int(scores[n])
    if score>high_score:
        high_score=score
print(f'Highest Score is {high_score}')