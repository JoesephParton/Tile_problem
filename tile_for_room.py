def tiles_in_room(r_width, r_length):
    width, length = 10, 25
    f_tiles_width = r_width // width
    f_tiles_length = r_length // length
    if r_width % width != 0:
        f_tiles_width += 1
    if r_length % length != 0:
        f_tiles_length += 1
    tiles = f_tiles_width * f_tiles_length
    return tiles


width = int(input("Width: "))
length = int(input("Length: "))
print(tiles_in_room(width, length))

