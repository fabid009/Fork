def sort():
	for i in range(0,n):
	       	ready_queue.append([priority[i],burst_time[i],process[i]])
	ready_queue.sort()
	for i in range(0,n):
		priority[i] = ready_queue[i][0]
		burst_time[i] = ready_queue[i][1]
		process[i] = ready_queue[i][2]
	print(" ")

process=[]
priority=[]
burst_time=[]
ready_queue=[]

n=0
a="p0"
b=1
c=2
inp=open("Input.txt","r")
for line in inp:
	a,b,c=line.split()
	process.append(a)
	priority.append(int(b))
	burst_time.append(int(c))
	
n=len(process)
print("Input read from file: ")
print("Process: " + str(process))
print("Priority: "+ str(priority))
print("BurstT:  " + str(burst_time))
print("")

sort()

print("After Swapping: ")
print("Process: " + str(process))
print("Priority: " + str(priority))
print("BurstT:  " + str(burst_time))
print("")

waiting_time=[]
turn_around_time=[]

waiting_time.insert(0,0)
turn_around_time.insert(0,burst_time[0])

for i in range(1,n):
	waiting_time.insert(i,waiting_time[i-1]+burst_time[i-1])
	turn_around_time.insert(i,waiting_time[i]+burst_time[i])

wsum=0.0
tsum=0.0

for i in range(0,n):
	print("Waiting time of " + str(process[i]) + " = " + str(waiting_time[i]))
 	print("TurnAround time of " + str(process[i]) + " = "+str(turn_around_time[i]))
	print("")

for i in range(0,n):
	wsum=wsum+waiting_time[i]
	tsum=tsum+turn_around_time[i]

print("Avg WaitingTime = " + str(float(float(wsum) / n)))
print("Avg TurnAroundTime = " + str(float(float(tsum) / n))) 
