def solution(string,markers):
    for marker in markers:
        for i in range(string.count(marker)):
            marker_index = string.index(marker)
            try:
                break_index = string[marker_index:].index('\n')
                string = string[:marker_index].rstrip(' ') + string[marker_index:][break_index:]
            except:
                string = string[:marker_index].rstrip(' ')
                                
    return string