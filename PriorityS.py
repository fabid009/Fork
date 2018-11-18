
process=[]
priority=[]
burstt=[]
pexecute=[]
n=0
a="p0"
b=1
c=2
inp=open("Input.txt","r")
for line in inp:
	a,b,c=line.split()
	process.append(a)
	pexecute.append(0)
	priority.append(int(b))
	burstt.append(int(c))
	
n=len(process)
print("Input read from file: ")
print("Process: " + str(process))
print("Priority: "+ str(priority))
print("BurstT:  " + str(burstt))
print("")

t_time=[]
w_time=[]

i=0
j=0
for i in range(len(priority)-1):
	for j in range(len(priority)-i-1):
		if(priority[j]>priority[j+1]):
			swap=priority[j]
			priority[j]=priority[j+1]
			priority[j+1]=swap

   			swap=burstt[j]
			burstt[j]=burstt[j+1]
			burstt[j+1]=swap

			swap=process[j]
			process[j]=process[j+1]
			process[j+1]=swap

w_time.insert(0,0)
t_time.insert(0,burstt[0])

i=1
for i in range(1,n):
	w_time.insert(i,w_time[i-1]+burstt[i-1])
	t_time.insert(i,w_time[i]+burstt[i])

sum1=0.0
sum2=0.0
i=0

for i in range(0,len(w_time)):
	print("Waiting time of " + str(process[i]) + " = " + str(w_time[i]))
 	print("TurnAround time of " + str(process[i]) + " = "+str(t_time[i]))
	print("")

for i in range(0,n):
	sum1=sum1+w_time[i]
	sum2=sum2+t_time[i]

print("Avg WaitingTime = " + str(float(float(sum1) / n)))
print("Avg TurnAroundTime = " + str(float(float(sum2) / n))) 
