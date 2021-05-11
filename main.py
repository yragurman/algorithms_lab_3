def distribution_of_clans(length_of_list, list_of_couples):
    list_of_clans = []
    for people in list_of_couples:
        if length_of_list > 1000:
            return -1
        for tribe in list_of_clans:
            if people[0] in tribe:
                tribe.add(people[1])
                break
            elif people[1] in tribe:
                tribe.add(people[0])
                break
        else:
            list_of_clans.append({people[0], people[1]})
    return list_of_clans


def count_boys_and_girls_inClan(clan):
    girls = 0
    boys = 0
    for human in clan:
        if human % 2 == 0:
            girls += 1
        else:
            boys += 1
    return girls, boys


def count_wedding_pairs(clans):
    boys = 0
    girls = 0
    sum_impossible_pair = 0
    for clan in clans:
        sum_girl_in_one_clan, sum_boys_in_one_clan = count_boys_and_girls_inClan(clan)
        boys += sum_boys_in_one_clan
        girls += sum_girl_in_one_clan
        sum_impossible_pair += sum_boys_in_one_clan * sum_girl_in_one_clan
    return boys * girls - sum_impossible_pair


if __name__ == '__main__':
    graph = [(1, 2), (2, 4)]
    print(count_wedding_pairs(distribution_of_clans(2, graph)))

