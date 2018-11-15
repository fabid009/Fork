class Queue:
	def __init__ (self):
		self.item = []

	def enqueue(self,item):
		self.item.insert(0,item)

	def dequeue(self):
		r = self.item.pop()
		if(r>0):
			return r
		else:
			return 0

print ("Enter no of processes : ")
n = int(input())

print ("Enter the quantum time : ")
quantum=int(input())

processes=[]
pexe=[]
bursttime=[]
arrivaltime =[]
completiontime=[]
turnaroundtime=[]
procesinqueue=[]

for i in range (0,n):
	processes.insert(i,i+1)
	pexe.insert(i,0)
	completiontime.insert(i,0)
	turnaroundtime.insert(i,0)
	procesinqueue.insert(i,0)
	bursttime.insert(i,int(raw_input("Enter burst time: ")))
	arrivaltime.insert(i,int(raw_input("Enter arrival time: ")))
	print("")

processingarray=[]
processingarray.insert(0,arrivaltime[0])
sum=arrivaltime[0]
sumindex=1

count = 0
q=Queue()
q.enqueue(processes[0])
procesinqueue[0]=1

while (count < n):
	d=q.dequeue()-1
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
			q.enqueue(processes[i])
			procesinqueue[i]=1
	if bursttime[d]==0:
		count += 1
		pexe[d]=1
		completiontime[d]=sum
	else:
		q.enqueue(processes[d])

for i in range (0,n):
	turnaroundtime[i]=completiontime[i]-arrivaltime[i]

sum1 = 0.0
for i in range(0,n):
	sum1 += turnaroundtime[i]
	print("TurnAroundTime of P" + str(processes[i]) + " = "+ str(turnaroundtime[i]))
	print("")

print("Avg TurnAroundTime = " + str(float(float(sum1) / n)))

