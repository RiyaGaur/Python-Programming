if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    def average(l):
        sum=0
        for i in l:
            sum+=i
            avg=sum/len(l)
        print('%.2f'%avg)

    for i in student_marks:
        if i==query_name:
            average(student_marks[i])
