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

print("Enter no. of processes: ")
n=int(input())

process=[]
pexecute=[]
order=[]
arrivalt=[]
burstt=[]
waitingt=[]

for i in range(0,n):
	process.insert(i,i+1)
	pexecute.insert(i,0)
	burstt.insert(i,int(raw_input("Enter Burst Time: ")))
	arrivalt.insert(i,int(raw_input("Enter Arrival Time: ")))
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
