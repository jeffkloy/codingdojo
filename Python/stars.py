x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(x):
    for item in x:
        if type(item) == int:
            item = "*" * item
        if type(item) == str:
            length = len(item)
            item = item[0].lower()
            item = item * length
        print item

draw_stars(x)