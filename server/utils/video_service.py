def create_search_string(title, genra, hash_tags):
    search_string = title
    title_split = title.split()
    for word in title_split:
        search_string += " " + word

    for tag in hash_tags:
        search_string += " " + tag

    for gen in genra:
        search_string += gen

    return search_string
