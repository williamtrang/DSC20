def colors(lst):
    colors_dict = {}
    for i in range(len(lst)):
        if lst[i][1] not in colors_dict:
            colors_dict[lst[i][1]] = []
        colors_dict[lst[i][1]].append(lst[i][0])
    return colors_dict