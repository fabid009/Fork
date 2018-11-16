class Queue:
	def __init__ (self):
		self.item = []

	def enqueue(self,item):
		self.item.insert(0,item)

	def dequeue(self):
		r = int(self.item.pop())
		if(r>0):
			return r
		else:
			return 0

#print ("Enter no of processes : ")
#n = int(input())

print ("Enter Time Quantum : ")
quantum=int(input())

process=[]
pexe=[]
bursttime=[]
arrivaltime =[]
completiontime=[]
turnaroundtime=[]
procesinqueue=[]

n=0
a="p0"
b=1
c=2
inp=open("Input.txt","r")
for line in inp:
	a,b,c=line.split()
	process.append(a)
	pexe.append(0)
	bursttime.append(int(b))
	arrivaltime.append(int(c))
	
n=len(process)
print("Input read from file: ")
print("Process: ",process)
print("BurstT:  ",bursttime)
print("Arrival: ",arrivaltime)
print("")

for i in range (0,n):
	completiontime.insert(i,0)
	turnaroundtime.insert(i,0)
	procesinqueue.insert(i,0)
	#bursttime.insert(i,int(raw_input("Enter burst time: ")))
	#arrivaltime.insert(i,int(raw_input("Enter arrival time: ")))

processingarray=[]
processingarray.insert(0,arrivaltime[0])
sum=arrivaltime[0]
sumindex=1

count = 0
q=Queue()
q.enqueue(process[0])
procesinqueue[0]=1
while (count < n):
	d=(q.dequeue())-1
	if pexe[d]!=1:
		if bursttime[d] < quantum:
			sum+=bursttime[d]
			bursttime[d] -= bursttime[d]
		else:
			sum+=quantum
			bursttime[d]-=quantum
		processingarray.insert(sumindex,sum)
		sumindex += 1
	for i in range(0,n):
		if arrivaltime[i] <= sum and procesinqueue[i] !=1:
			q.enqueue(process[i])
			procesinqueue[i]=1
	if bursttime[d]==0:
		count = count + 1
		pexe[d]=1
		completiontime[d]=sum
	else:
		q.enqueue(process[d])

for i in range (0,n):
	turnaroundtime[i]=completiontime[i]-arrivaltime[i]

sum1 = 0.0
for i in range(0,n):
	sum1 += turnaroundtime[i]
	print("TurnAroundTime of " + str(process[i]) + " = "+ str(turnaroundtime[i]))
	print("")

print("Avg TurnAroundTime = " + str(float(float(sum1) / n)))

