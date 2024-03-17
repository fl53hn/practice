def solution(w,h):
    def gcd(a, b):
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                return i
    
    JS = gcd(w, h)
    print(w)
    print(JS)
    print(w//JS)
    answer = w*h - (((w/JS) * (h/JS)) - ((w/JS)-1) * ((h/JS)-1))*JS
    return answer
