def follow(instructions):
    return (instructions.count("r")-instructions.count("l"), instructions.count("f")-instructions.count("b"))