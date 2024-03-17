def solution(cacheSize, cities):
    answer = 0
    cache = []
    user_data = []
    for i in range(len(cities)):
        user_data.append(cities[i].lower())
    for data in user_data:
	# Miss!
        if data not in cache:
            if len(cache) < cacheSize:
                answer +=5
                cache.append(data)
            elif cacheSize == 0:
                answer +=5
            else:
                answer +=5
                cache.pop(0)
                cache.append(data)
	# Hit!
        else:
            answer +=1
            cache.pop(cache.index(data))
            cache.append(data)
    return answer
