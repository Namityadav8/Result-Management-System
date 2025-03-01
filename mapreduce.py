from mrjob.job import MRJob

class MarksTotal(MRJob):

    def mapper(self, _, line):
        try:
            import json
            student = json.loads(line)
            yield student["StudentID"], sum(student["Marks"].values())
        except:
            pass

    def reducer(self, student_id, marks):
        yield student_id, sum(marks)

if __name__ == "__main__":
    MarksTotal.run()