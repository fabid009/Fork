def sort():
	for i in range(0,n):
	       	ready_queue.append([burst_time[i],arrival_time[i],process[i]])
	ready_queue.sort()
	for i in range(0,n):
		burst_time[i] = ready_queue[i][0]
		arrival_time[i] = ready_queue[i][1]
		process[i] = ready_queue[i][2]
	print(" ")

process=[]
ready_queue=[]
arrival_time=[]
burst_time=[]

a="p0"
b=0
c=0
n=0
inp=open("Input.txt","r")
for line in inp:
	a,b,c=line.split()
	process.append(a)
	arrival_time.append(int(b))
	burst_time.append(int(c))
	
n=len(process)

print("Input read from file: ")
print("Process: " + str(process))
print("ArrivalT: " + str(arrival_time))
print("BurstT:  " + str(burst_time))
print("")

sort()

print("After Swapping: ")
print("Process: " + str(process))
print("ArrivalT: " + str(arrival_time))
print("BurstT:  " + str(burst_time))
print("")

time_of_completion=0
waiting_time=[]
turn_around_time=[]
tat=0
waiting_time.insert(0,0)

for i in range(0,n):
	time_of_completion = time_of_completion + burst_time[i]	
	waiting_time.insert(i+1,time_of_completion)
	if(time_of_completion>arrival_time[i]):
		tat = time_of_completion-arrival_time[i]
	else:
		tat = arrival_time[i] - time_of_completion
	turn_around_time.insert(i,tat)

wsum=0.0
tsum=0.0

for i in range(0,len(waiting_time)-1):
	if(waiting_time[i]>arrival_time[i]):
		waiting_time[i] = waiting_time[i] - arrival_time[i]
	else:
		waiting_time[i] = arrival_time[i] - waiting_time[i]
	wsum = wsum + waiting_time[i]
	tsum = tsum + turn_around_time[i]
	print("Waiting time of " + str(process[i]) + " = " + str(waiting_time[i]))
     	print("TurnAroundTime time of " + str(process[i]) + " = " + str(turn_around_time[i]))
	print("")
print("Avg waiting time = " + str(float(float(wsum)/n)))
print("Avg turnaround time = "+ str(float(float(tsum)/n)))
