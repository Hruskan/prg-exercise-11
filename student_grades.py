from sorting import bubble_sort, random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
    def get_by_index(self, index):
        return self.scores[index]
    def count(self):
        return len(self.scores)
    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"
    def find(self, score):
        indexes = []
        for i in range(len(self.scores)):
            if self.scores[i] == score:
                indexes.append(i)
        return indexes
    def get_sorted(self):
        scores = self.scores.copy()
        return bubble_sort(scores)

def main():
   results = StudentsGrades(random_numbers(30, 0, 100))
   print(results.count())
   for i in range(len(results.scores)):
       print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")
   print(f"Studenti s plným počtem bodů: {results.find(100)}")
   print(f"Seřazená skóre: {results.get_sorted()}")


if __name__ == '__main__':
    main()