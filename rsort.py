import re
import sys


def sort_requirements(path):
    lines = []
    lib_block = []

    with open(path, "r+") as f:
        for line in f.readlines() + [""]:
            if re.findall("^#|^$", line):  # if comment or empty line
                lines += sorted(
                    lib_block,
                    key=lambda line: re.split("==|<=|>=|~=|<|>", line, maxsplit=1)[0],
                )
                lines.append(line)
                lib_block = []
            else:
                lib_block.append(line)

        f.seek(0)
        f.writelines(lines)


if __name__ == "__main__":
    path = "requirements.txt"

    if len(sys.argv) == 2:
        path = sys.argv[1]

    sort_requirements(path=path)

    print("{} has been sorted".format(path))
