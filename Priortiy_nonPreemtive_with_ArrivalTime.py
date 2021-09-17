import numpy as np


def find_waiting_time2(n, pro, at, bt, priority, wt):
    t = 0
    waitTime = 0
    burstTime = 0
    bt1 = bt.copy()
    
    for i in range(n):
        for j in range(n):
            if at[j] <= t and bt[j] != 0:

                if t == 0:                    
                    wt[0] = 0
                    waitTime = 0
                    burstTime = bt[j]
                    
                else:
                    wt[j] = waitTime+burstTime
                    waitTime = wt[j]
                t += bt1[j]
                burstTime = bt1[j]
                bt1[j] = 0

            else:
                pass
        break


def find_waiting_time3(n, pro, at, bt, priority, wt):
#first bring process with lowest arrival time
    pro2 = [x for _, x in sorted(zip(at, pro))]
    bt2 = [x for _, x in sorted(zip(at, bt))]
    #priority = [x for _, x in sorted(zip(at, priority))]
    at2= at.sort()

# 2nd run that process and make burst time zero
    t=at[0]
    bt2[0]=0
    wt[0]=0


def find_waiting_time(n, pro, at, bt, priority, wt):
    #gc=np.zeros((2,n),dtype=np.int32)
    bt2=bt.copy()
    gc=[0]
    t=min(at)

    x=at.index(t)

    gc[0]=t
    gc.append(bt2[x])
    t+=gc[1]
    bt2[x]=0
    i=0

    while(len(gc)!=n):
        if at[i]<=t and bt2[i]!=0:
            gc.append(gc[-1]+bt2[i])
            bt2[i]=0
            t=gc[-1]
            i=0
        else:
            i+=1
    #print(gc)
    #print(pro)

    pro = (pro[n - 1:n] + pro[ 0: n-1])
    priority = (priority[n - 1:n] + priority[ 0: n-1])
    bt  = (bt [n - 1:n] + bt [ 0: n-1])
    at = (at[n - 1:n] + at[ 0: n-1])

    wt[0]=0
    
    for i in range(1,n):
        wt[i]=gc[i]-at[i]
        
    #print(wt)


def find_turn_around_time(n, wt, bt, tat):
    for i in range(n):
        tat[i] = wt[i]+bt[i] 
    print(tat)


def find_average_time(n, pro, at, bt, priority):
    tat = [0]*n
    wt = [0]*n

    find_waiting_time(n, pro, at, bt, priority, wt)
    find_turn_around_time(n, wt, bt, tat)

    

    # print the table
    print("Process  \t Burst time \t Waiting time \t Turn Around Time")
    for i in range(n):
        print(pro[i], '\t', '\t', bt[i], '\t', '\t', wt[i], '\t', '\t', tat[i])
    total_tat=0
    total_wt=0

    for i in range(n):
        total_tat+=tat[i]
        total_wt+=wt[i]
    
    print("Average turn around time is",total_tat/n)
    print("Average waiting time is",total_wt/n)


if __name__ == '__main__':
    processes = [1, 2, 3, 4, 5]
    priority = [5,4,3,1,2]
    arrival_time = [0, 1, 2, 3, 4]
    burst_time = [4,3,1,5,2]
    n = len(processes)
    # sort all on basis of priority

    pro = [x for _, x in sorted(zip(priority, processes))]
    at = [x for _, x in sorted(zip(priority, arrival_time))]
    bt = [x for _, x in sorted(zip(priority, burst_time))]
    priority.sort()

    find_average_time(n, pro, at, bt, priority)
