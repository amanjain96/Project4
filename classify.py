def love(lyrics):
    love_count = 0
    for word in lyrics.split():
        if word in ['love', 'kiss', 'dream']:
            love_count += 1
        else:
            continue
    
    return love_count
