import re


def getEm(filepath):
    with open(filepath, "r+", encoding='utf-8')as rfile:
        with open("savepolymers.txt", "a+", encoding='utf-8')as wfile:
            for line in rfile.readlines():
                if re.findall(r'(.*)@(.*)', line):
                    wfile.write(line[3:])

                else:
                    pass


def findRP(Filepath):
    Embuffer = []
    with open(filepath, "r+") as rfile:
        for line in rfile.readlines():
            line = line.replace("\n","")

            linebuff = line.split(";")

            for item in linebuff:
                if len(item) != 0:
                    if item not in Embuffer:
                        Embuffer.append(item)
                    else:
                        pass
                else:
                    pass
    
    with open("savepolymersEM.txt", "w+", encoding='utf-8')as wfile:
        for em in Embuffer:
            wfile.write(em + "\n")

if __name__ == "__main__":
    filebuffer ="polymers"
    for i in range(1, 6):
        filepath = "polymers"+ str(i) + ".txt"

        getEm(filepath)


    Filepath = "savepolymers.txt"
    findRP(Filepath)