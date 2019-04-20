def love(lyrics):
    love_count = 0
    for word in lyrics.split():
        if word in ['love', 'kiss', 'dream','amour','yearning','sex','like','babe','baby','girlfriend','boyfriend']:
            love_count += 1
    
    return love_count

def kid_safe(lyrics):
    kid_count = 0
    for word in lyrics.split():
        if word in ['fuck','bitch','shit','ass','asshole','fag','jerkoff','whore','cunt','pussy','arse']
            kid_count = 0

    return kid_count

def length(lyrics):
    length = 0
    for word in lyrics.split():
        length += 1

    return length

def complex(lyrics):
    complexity = 0
    for word in lyrics.splitlines():
        if word in ['is like','yo yo yo','uptown funk']: #we need to split in lines instead of words and check metaphors, alliterations,etc
            complexity +=1

    return complexity

def mood(lyrics):
    mood = 0
    for word in lyrics.split():
        if word in ['upbeat','happy','brilliant','energetic', 'enthusiastic']:
            mood +=1

    return mood
