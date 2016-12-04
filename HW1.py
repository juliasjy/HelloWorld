import sys
import subprocess

def main():
    argv = sys.argv
    # argv = str(' -f 1234567 -s Note')
    shaRepo = argv[4: 11]
    stringForSearch = argv[15: ]
    print(shaRepo)
    print(stringForSearch)

    SHAs = []
    cmd = 'git cat-file -p ' + shaRepo
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in output.stdout.readline():
        print(line)
        SHAs.append(line[12:30])

    for SHA in SHAs:
        if SHA[7: 10] == 'blob':
            cmd = 'git cat-file -p ' + SHA + ' | grep ' + stringForSearch
            output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(output.stdout.read())
        else:
            main()


