'''
Created on Feb 5, 2017
@author: suj1
'''
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser();
    parser.add_argument("-r", "--remote", help="the repo to pull to");
    args = parser.parse_args();
    localBranches = getLocalBranch();
    remoteBranches = getRemoteBranch(args.remote);
    pushToRemoteBranch(localBranches, remoteBranches, args.remote);

def getLocalBranch():
    localBranch = runCommand("git branch");
    localBranchResult = [];
    for branch in localBranch:
        branch = branch.strip();
        if(branch[:2] == "* "):
            localBranchResult.append(branch[2:]);
        else:
            localBranchResult.append(branch);
    return localBranchResult;

def getRemoteBranch(remoteBranch):
    remoteBranch = runCommand("git ls-remote --heads " + remoteBranch);
    remoteBranchResult = [];
    for branch in remoteBranch:
        branch = branch.split("\t")[1].strip().split("/")[-1];
        remoteBranchResult.append(branch);
    return remoteBranchResult;

def pushToRemoteBranch(localBranches, remoteBranches, remoteAddr):
    branchesToPush = list(set(localBranches) - set(remoteBranches));
    for branch in branchesToPush:
        print("git push " + remoteAddr + " " + branch);
        runCommand("git push " + remoteAddr + " " + branch + " " + branch);

def runCommand(cmd):
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
    return [line.decode('utf-8') for line in output.stdout];

if __name__ == "__main__":
    main()
