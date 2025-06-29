
def generateTable(n):
    t = ""
    for i in range(1,11):
        t += f"{n} x {i} = {n * i}\n"

    with open(f"Questions/FileIO/Tables/table_{n}.txt", "w") as f:
        f.write(t)

for i in range(2,21):
    generateTable(i)