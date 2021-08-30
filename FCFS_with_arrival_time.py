
def findWaitingTime(processes,n,bt,at,wt):

    sum_burst_time=[0]*n
    wt[0]=at[0]

    #first we will find sum of all burst time fill i'th postition and store it in sum_bt[i]
    for i in range(1,n):
        sum_burst_time[i]= sum_burst_time[i-1] + bt[i-1]

    for i in range(n):
        wt[i]=sum_burst_time[i] - at[i]

        if(wt[i]<0):
            wt[i]=0
            

def findTurnAroundTime(processes,n,bt,tat,wt):

    for i in range(n):
        tat[i]=wt[i]+bt[i]



def findAverageTime(processes,n,bt,at):
    wt=[0]*n
    tat=[0]*n
    total_tat=0
    total_wt=0

    findWaitingTime(processes,n,bt,at,wt)
    findTurnAroundTime(processes,n,bt,tat,wt)

    for i in range(n):
        total_tat+=tat[i]
        total_wt+=wt[i]


    #print the table
    print("Process \t Arrival Time \t Burst time \t Waiting time \t Turn Around Time")
    for i in range(n):
        print(processes[i],'\t','\t','\t',at[i],'\t','\t',bt[i],'\t','\t',wt[i],'\t','\t',tat[i])


    print("Average turn around time is",total_tat/n)
    print("Average waiting time is",total_wt/n)




if __name__ == '__main__':
    processes = [1, 2, 3, 4]
    burst_time = [5, 3, 8, 6]
    arrival_time = [0, 1, 2, 3]
    n=len(processes)
    findAverageTime(processes,n,burst_time,arrival_time)