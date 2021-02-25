import os
import sys
import subprocess

def system_command(command):
    os.system(command)

def iterate_file(buildfile):
    with open(buildfile) as BUILDFILE:
        for x in BUILDFILE.readlines():
            x = x.strip("\n")

            if not x.startswith("//") and x != "":
                x = x.split(",")

                for y in x:
                    y.strip("\n")

                #print(x)

                if x[0] == "pull":
                    del x[0]
                    system_command("git pull " + " ".join(x))
                
                elif x[0] == "push":
                    del x[0]
                    system_command("git push " + " ".join(x))
                
                elif x[0] == "gpp":
                    system_command(f"g++ \"{x[1]}\" -o \"{x[2]}\"")
                
                elif x[0] == "exec":
                    del x[0]
                    system_command(" ".join(x))
                
                elif x[0] == "add":
                    del x[0]
                    system_command("git add " + " ".join(x))
                
                elif x[0] == "commit":
                    if len(x) >= 2:
                        system_command("git commit -m")
                    system_command("git commit -m \"" + input("Commit name> ") + "\"")
                
                else:
                    print("[Buildfile/Error] ERROR IN BUILDFILE")
                    quit()

def main():
    print("[Buildfile/Info] Builder.")
    iterate_file(sys.argv[1])
    print("[Buildfile/Info] Exited.")

main()