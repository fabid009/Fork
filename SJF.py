def returnFirstbursttime():
    for i in range(0,len(burstt)):
        if pexecute[i] != 1:
            return i

def returnIndexOfLowesetBurst():
    min = returnFirstbursttime()
    for i in range(returnFirstbursttime() + 1,len(burstt)):
        if burstt[i] < burstt[min] and pexecute[i] != 1:
            min = i
    pexecute[min] = 1
    return min

# print("Enter the number of process:")
# n = int(input())
process = []
pexecute = []
burstt = []
arrivalt = []

n=0
a="p0"
b=1
c=2
inp=open("Input.txt","r")
for line in inp:
	a,b,c=line.split()
	process.append(a)
	pexecute.append(0)
	burstt.append(int(b))
	arrivalt.append(int(c))
	
n=len(process)
print("Input read from file: ")
print("Process: ",process)
print("BurstT:  ",burstt)
print("Arrival: ",arrivalt)
print("")

#for i in range(0,n):
#	processes.insert(i,i+1)
#       pexecute.insert(i,0)
#       burstt.insert(i,int(raw_input("Enter burst time: ")))
#       arrivalt.insert(i,int(raw_input("Enter arrival Time: ")))
#	print("")

sum = 0
waitingt = []
runningProcess = []
turnAroundt = []
waitingt.insert(0,0)

for i in range(0,n):
	proces = returnIndexOfLowesetBurst()
	runningProcess.insert(i,proces+1)
        sum += burstt[proces]
	waitingt.insert(i+1,sum)
	turnAroundt.insert(i,sum-arrivalt[i])

sum1 = 0.0
sum2 = 0.0

for i in range(0,len(waitingt) - 1):
	sum1 += waitingt[i] - arrivalt[i]
	sum2 += turnAroundt[i]
	print("Waiting time of P" + str(runningProcess[i]) + " is "+ str(waitingt[i] - arrivalt[i]))
	print("Arrival time of P" + str(runningProcess[i]) + " = "+ str(turnAroundt[i]))
	print("")

print("Avg WaitingTime = " + str(float(float(sum1) / n)))
print("Avg TurnAroundTime = " + str(float(float(sum2) / n)))



