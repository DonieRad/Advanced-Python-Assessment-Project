# TASK 1 #

class Student:
    """
    This class represents a student with a name and a list of scores.
    It provides a method to evaluate the student's performance based on their average score.
    """
    def __init__(self, name, scores):
        # store name and scores as instance variables
        self.name = name
        self.scores = scores
    def evaluate_performance(self):
        # calculate the average score
        avg_score = sum(self.scores) / len(self.scores)

        # checking the performance level
        if avg_score >= 75:
            print(f'{self.name}: Excellent Performance')
        elif avg_score >= 50:
            print(f'{self.name}: Satisfactory Performance')
        else:
            print(f'{self.name}: Needs Improvement')

# create a student object with a name and scores
student1 = Student('David', [80, 90, 75, 60])

# call the method to evaluate performance
student1.evaluate_performance()