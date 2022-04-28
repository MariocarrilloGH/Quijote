import random
import sys

def main(filename, new_filename, prob):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    new_file = open(new_filename,"w")
    for i in lines:
        if random.random() < prob:
            new_file.write(i)
    new_file.close()

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 {0} <file>".format(sys.argv[0]))
    else:
        main("quijote.txt", sys.argv[1], 0.25)