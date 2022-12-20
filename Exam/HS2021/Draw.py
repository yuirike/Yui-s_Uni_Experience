def draw(size, instructions):
    for i in instructions:
        if instructions[0] > size-1:
            raise IndexError
        if instructions[1] > size-1:
            raise IndexError
        if len(instructions[2]) >= 1:
            raise ValueError

    