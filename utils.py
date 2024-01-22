def format_bits_to_gigabytes(bits):
    return int(bits) / 1024 ** 3


def get_random_memory_type(code):
    code = int(code)
    if code == 21:
        return "DDR"
    elif code == 22:
        return "DDR2"
    elif code == 24:
        return "DDR3"
    elif code == 26:
        return "DDR4"
    elif code == 20:
        return "SDRAM"
    elif code == 19:
        return "EDO"


def remove_empty_values(iterable):
    output = [line.strip() for line in iterable if line.strip()]
    return output


def get_lines_stdout(stdout: str):
    output = []
    values = []

    lines = stdout.split('\n')
    cleaned_list = remove_empty_values(lines)
    keys = remove_empty_values(cleaned_list[0].split(" "))

    for el in cleaned_list[1:]:
        values.append(remove_empty_values(el.split(" ")))

    for value in values:
        line = {}
        for matchKey in range(len(keys)):
            line[keys[matchKey]] = value[matchKey]
        output.append(line)

    return output


