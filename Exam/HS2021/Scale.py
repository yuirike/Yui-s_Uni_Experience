
def scale_up(factor, image):
    canvas = []
    image = image.split("\n")
    for line in image:
        new_line = []
        for char in line:
            new_line.append(char*factor)
        new_line = "".join(new_line)
        for i in range(factor):
            canvas.append(new_line)
    return "\n".join(canvas)




img1 = ("xxx\n"
       "x x\n"
       "xxx")


print(scale_up(2,img1))


img2 = ("xxxxxx\n"
        "xxxxxx\n"
       "xx  xx\n"
       "xx  xx\n"
       "xxxxxx\n"
       "xxxxxx")

print(img2)