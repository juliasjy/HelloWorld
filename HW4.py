'''
Created on Jan 7, 2017
@author: suj1
'''
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser();
    parser.add_argument("-u", "--use", help="SHA unmodified");
    parser.add_argument("-c", "--commitify", help="SHA insert as comments");
    parser.add_argument("-b", "--branch", help="Output branch");
    parser.add_argument("-p", "--prefix", help="Prefix String");
    args = parser.parse_args();
    merge(args.use, args.commitify, args.branch, args.prefix);

def merge(commit_default, commit_addition, output_branch, prefix):
    run_command("git branch " + output_branch + " " + commit_default);
    run_command("git checkout " + output_branch);
    run_command("git merge " + commit_addition);
    files = run_command("git diff --name-only --diff-filter=U");
    writefile(files, prefix);

def run_command(cmd):
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
    return output.stdout.read().split("\n");

def writefile(files, prefix):
    for file in files:
        new_file = "";
        flag = False;
        with open(file, "w") as file_lines:
            for line in file_lines:
                if ((">>>>>>>" in line) or ("<<<<<<<" in line)):
                    flag = False;
                elif ("=======" in line):
                    flag = True;

                if (flag):
                    new_file.append(prefix + line)
                else:
                    new_file.append(line)

            file.write(new_file);
            file.close();

if __name__ == "__main__":
    main()
