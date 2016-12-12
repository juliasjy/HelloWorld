"""
<describe what this module has/does>

Created on Dec 11, 2016.
Written by: suj1.
"""
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser();
    parser.add_argument('-t', '--treeSHAs', help='Get a series of trees', action='append')
    parser.add_argument('-o', '--output', help='Get the sha of output')
    args = parser.parse_args();
    parentSHA = commitTree(args)
    updateRef(args, parentSHA)

def commitTree(args):
    parentSHA = None
    for treeSHA in args.treeSHAs:
        if parentSHA == None:
            cmd = 'git commit-tree ' + treeSHA + '-m "alternative begin"'
            output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            parentSHA = output.stdout.readline()
        else:
            cmd = 'git commit-tree ' + treeSHA + '-p' + parentSHA + '-m "alternative followup"'
            output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(output.stdout.read())
            parentSHA = output.stdout.readline()
    return parentSHA

def updateRef(args, parentSHA):
    cmd = 'git update-ref refs/heads/' + args.output + ' ' + parentSHA
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
