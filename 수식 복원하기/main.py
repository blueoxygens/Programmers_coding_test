def d_to_b(num, base):
    if num == 0: return "0"
    digits = "0123456789"
    result = ""
    while num > 0:
        num, remainer = divmod(num, base)
        result = digits[remainer] + result
    return result

def solution(expressions):
    min_base = 2
    for e in expressions:
        for char in e:
            if char.isdigit():
                min_base = max(min_base, int(char) + 1)
    
    candidate = [b for b in range(min_base, 10)]
    
    for e in expressions:
        l = e.split(" ")
        if l[4] == "X": continue
        
        next_candidate = []
        for c in candidate:
            try:
                v1, v2, res = int(l[0], c), int(l[2], c), l[4]
                target = v1 + v2 if l[1] == "+" else v1 - v2
                if d_to_b(target, c) == res:
                    next_candidate.append(c)
            except ValueError:
                continue
        candidate = next_candidate

    answer = []
    for e in expressions:
        l = e.split(" ")
        if l[4] != "X": continue
        
        results = set()
        for c in candidate:
            v1, v2 = int(l[0], c), int(l[2], c)
            target = v1 + v2 if l[1] == "+" else v1 - v2
            results.add(d_to_b(target, c))
        
        final_res = results.pop() if len(results) == 1 else "?"
        answer.append(f"{l[0]} {l[1]} {l[2]} = {final_res}")
        
    return answer