# AvC Nuke

power = 5 # WARNING: Increasing this value may crash your computer

def nuke(n):
    a=[]
    for i in range(10):
        if(n>1):
            a.append(nuke(n-1))
        else:
            a.append(i)
    return a

print(nuke(power))
