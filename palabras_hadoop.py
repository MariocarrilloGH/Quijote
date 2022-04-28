from pyspark import SparkContext
import sys

def main(filename, new_filename):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(filename)
        words_rdd = data.map(lambda x: len(x.split()))
        f = open(new_filename,"w")
        f.write(str(words_rdd.sum()))
        f.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 {0} <file>".format(sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])