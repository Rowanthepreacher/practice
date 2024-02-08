from random import randint

def collateresults(dicetypes, times):
    for dtype in dicetypes:
        rollaverageexp = []
        rollaveragebump = []
        for count in range(times):
            finalrollexp = rolldice(dtype)
            finalrollbump = rollnoexplode(dtype)
            rollaverageexp.append(finalrollexp)
            rollaveragebump.append(finalrollbump)
        rollaverageexp = sum(rollaverageexp)/len(rollaverageexp)
        rollaveragebump = sum(rollaveragebump)/len(rollaveragebump)
        print(f"I rolled a d{dtype} {times} times and the average was {rollaverageexp}")
        print(f"I rolled a d{dtype} {times} times and the average was {rollaveragebump}")
        print(f"Over the course of {times} rolls of a d{dtype}, the difference between averages was {rollaverageexp - rollaveragebump}.")


def rolldice(dtype):
    rolloutput = randint(1,dtype)
    if rolloutput == dtype:
        rolloutput == rolloutput + rolldice(dtype)
    return rolloutput

def rollnoexplode(dtype):
    noexplode = randint(1,dtype)
    if noexplode <= 2:
        noexplode == 3
    return noexplode

collateresults([4,6,8,10,12],10000)