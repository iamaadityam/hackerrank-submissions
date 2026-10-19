def split_and_join(line):
    # write your code here
    out = ""
    for i in range(len(line.split())):
        out = out + line.split()[i] + "-"
    return(out[:-1])
if __name__ == '__main__':