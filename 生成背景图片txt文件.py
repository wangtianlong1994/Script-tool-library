import os

file_name = os.listdir("./beijing")

for b in file_name:

    f = open("1.txt", "a")

    f.write("data/images/train/beijing/"+b+"\n")
    #
    # print(s)
    # print()
    # a = s.split(" ")[0]
    # for i in a.split("\n"):
    #     p = i+".jpg"+"\n"
    #
    #     o = open("1.txt", "a")
    #     o.write(p)
f.close()
    # o.close()
