import random

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
    main("quijote.txt", "quijote_s05.txt", 0.25)