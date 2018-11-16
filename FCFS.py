def returnFirstarrivaltime():
    for i in range(0,len(arrivalt)):
        if pexecute[i] != 1:
            return i

def returnIndexOfLowestOrder():
    min = returnFirstarrivaltime()
    for i in range(returnFirstarrivaltime() + 1,len(arrivalt)):
        if arrivalt[i] < arrivalt[min] and pexecute[i] != 1:
            min = i
    pexecute[min] = 1
    return min

process=[]
pexecute=[]
order=[]
arrivalt=[]
burstt=[]
waitingt=[]
n=0
a="p0"
b=1
c=2
inp=open("input.txt","r")
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

for i in range(0,n):
	order.insert(i,arrivalt[i])

def swap(t1,t2):
	return t2,t1

sum=0
waiting=[]
runningprocess=[]
turnaroundt=[]
waiting.insert(0,0)
for i in range(0,n):
	proces=returnIndexOfLowestOrder()
	runningprocess.insert(i,proces+1)
	sum+=burstt[proces]	
	waiting.insert(i+1,sum)
	if(arrivalt[i]>sum):
		turnaroundt.insert(i,arrivalt[i]-sum)
	else:
		turnaroundt.insert(i,sum-arrivalt[i])

sum1=0.0
sum2=0.0

for i in range(0,len(waiting)-1):
	if(waiting[i]>arrivalt[i]):
		sum1+=waiting[i]-arrivalt[i]
	else:
		sum1+=arrivalt[i]-waiting[i]
	sum2+=turnaroundt[i]
        if(waiting[i]>arrivalt[i]):
		print("Waiting time of P" + str(runningprocess[i]) + " = " + str(waiting[i]-arrivalt[i]))
        else:
		print("Waiting time of P" + str(runningprocess[i]) + " = " + str(arrivalt[i]-waiting[i]))
 	print("TurnAroundTime time of P" + str(runningprocess[i]) + " = " + str(turnaroundt[i]))
	print("")
print("Avg waiting time = " + str(float(float(sum1)/n)))
print("Avg turnaround time = "+ str(float(float(sum2)/n)))
