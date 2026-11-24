#=======================================================================================================================
#Programmer: Nathalie Kate B. Subido
#Section: 8-Sampaguita
#Date: 11/24/2026
#Activity: Activity 7 - List Activity
#Description:  Python program that stores quiz scores in a list and generates a performance report.
#=======================================================================================================================

quiz_score = []

for i in range(1,6):
    quiz_score.append(int(input(f"Enter quiz score number {i}: ")))

print("="*30)
print(" QUIZ SCORE REPORT")
print("="*30)
print(f"Quiz scores:{quiz_score}")
print(f"Number of quizzes: 5")
print(f"Total Score: {sum(quiz_score)}")
print(f"Average Score: {sum(quiz_score) / len(quiz_score):.2f}")
print(f"Highest Score: {max(quiz_score)}")
print(f"Lowest Score:{min(quiz_score)}")
print(f"Ascending: {sorted(quiz_score)}")
print(f"Decending: {sorted(quiz_score, reverse=True)}")
print(f"Original Score: {quiz_score}")