import sys
import subprocess

def main():
    argv = sys.argv
    shaRepo = argv[2]
    stringForSearch = argv[4]
    searchTree(shaRepo, stringForSearch)

def searchTree(sha, stringForSearch):
    cmd = 'git cat-file -p ' + sha
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in output.stdout.readlines():
        strs = line.split()
        SHA = strs[2]
        if strs[1] == 'blob':
            cmd1 = 'git cat-file -p ' + SHA + ' | grep ' + stringForSearch
            output1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            s = output1.stdout.read();
            if len(s) > 0 :
                print s,
            elif strs[1] == 'tree':
                searchTree(SHA, stringForSearch)

if __name__ == "__main__":
        main()