

def find_wt(n,wt,bt):
    t=0
    for i in range(n):
        t+=bt[i]
        if(i==0):
            wt[0]=0
        else:
            wt[i]=wt[i-1]+bt[i-1]

def find_tat(n,wt,bt,tat):
    for i in range(n):
        tat[i]=bt[i]+wt[i]
    

def findAverageTime(n,pro,bt,priority):
    wt=[0]*n
    tat=[0]*n

    find_wt(n,wt,bt)
    find_tat(n,wt,bt,tat)

    #print the table
    print("Process  \t Burst time \t Waiting time \t Turn Around Time")
    for i in range(n):
        print(pro[i],'\t','\t',bt[i],'\t','\t',wt[i],'\t','\t',tat[i])




if __name__ == '__main__':
    processes = [1, 2, 3]
    burstTime = [10,5,8]
    priority = [1,3,2]
    n=3
    #sort the processess on basis of priority
    pro=[x for _,x in sorted(zip(priority,processes))]
    bt=[x for _,x in sorted(zip(priority,burstTime))]
    priority.sort()

    findAverageTime(n,pro,bt,priority)