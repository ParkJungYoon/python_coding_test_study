def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    days = sum(day[:a-1])+b-1
    return week[days%7]