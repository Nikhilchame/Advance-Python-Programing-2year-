def count_lines(path):
    with open(path, "r") as f:
        return sum(1 for _ in f)


def extract_first_lines(path, n=2):
    lines = []
    with open(path, "r") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line)
    return lines


def write_lines(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)


if _name_ == "_main_":
    input_file = "input.txt"
    output_file = "output_first_two_lines.txt"

    print("Total lines:", count_lines(input_file))

    lines = extract_first_lines(input_file, 2)
    write_lines(output_file, lines)

    print("First two lines written successfully!")