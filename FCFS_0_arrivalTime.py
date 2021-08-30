# create a python script to find average waiting time and 
# average Turn around time of proccess by first come first serve scheduling


def findWaitingTime(processes,n,bt,wt):
    wt[0]=0  #since 1st process will not wait and will start immediately

    #for rest of processess      waiting time= (burst time of previous process) + (waiting time of previous process)

    for i in range(1,n):
        wt[i]=bt[i-1] + wt[i-1]

def findTurnAroundTime(processes,n,bt,wt,tat):
    
    #turn around time = (time process waits in queue)+ (time taken to complete the process)
    for i in range(n):
        tat[i]=wt[i]+bt[i]
        

#funtion to calculater average times
def findAverageTime(processes,n,bt):
    wt=[0]*n #waiting time list of size n
    tat=[0]*n #turn around time list of size n
    total_wt=0
    total_tat=0

    #now find waiting time array and tat array by creating different functions
    #step I-> find waiting time for each process
    findWaitingTime(processes,n,bt,wt)
    #step II-> find Turn around time for each process
    findTurnAroundTime(processes,n,bt,wt,tat)

    #now to calculate total WT and TAT
    for i in range(n):
        total_tat+=tat[i]
        total_wt+=wt[i]

        #print the table
    print("Process \t Burst time \t Waiting time \t Turn Around Time")
    for i in range(n):
        print(processes[i],'\t','\t','\t',bt[i],'\t','\t',wt[i],'\t','\t',tat[i])


    print("Average waiting time is",(total_wt/n))
    print("Average turn around time is",(total_tat/n))




if __name__=='__main__':
    processes=[1,2,3,4,5] #number of processes
    n=len(processes)
    # print(n)
    burstTime=[8,1,3,2,6]

    #call function to find average time
    findAverageTime(processes,n,burstTime)
