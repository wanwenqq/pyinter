# coding = utf-8


if __name__ == "__main__":
    with open('D:/temper/demo.txt') as f:
        for line in f.readlines():
            print(line.strip())