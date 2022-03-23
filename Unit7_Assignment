'''Connor Fisher IT244 Python Programming Purdue
    Unit 7 Assignment created 20220320'''
#Program  to determine if you are over, under, or at par on 3 different golf holes. 
#Class being defined.
class golf:
    'Score is at, under, or over par' #doc string
    results = " "
#Initializing variables
    def __init__(self, hole, score, par):
        self.hole = hole
        self.par = par
#Defining constructor     
    def eval_Display(self, hole, score):
        #evaluating
        if (score > self.par):
            golf.results = "Over Par"
        elif (score < self.par):
            golf.results = "Under Par"
        else:
            golf.results = "At Par"
        #displaying
        print("You score is", golf.results, "on hole", hole, "which had a par of", self.par)
#Initialization of score
score = 0
#Objects being created
score1 = golf("1", score, 3)
score2 = golf("2", score, 4)
score3 = golf("3", score, 5)
#Prompt for hole and score
userHole = int(input("Enter which hole you would like to check (1, 2, or 3):  "))
score = int(input("Enter the score you achieved on the hole: "))
#evaluating the hole (object for class)
if userHole == 1:
    score1.eval_Display("1", score)
elif userHole == 2:
    score2.eval_Display("2", score)
elif userHole == 3:
    score3.eval_Display("3", score)
