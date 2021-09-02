
def find_waiting_time(wt,bt,n,q):

    rem_bt=[0]*n
    rem_bt=bt.copy()            # make a copy of burst time to us it for calculation and reduction in each step

    # loop untill  all process are completed i.e. rem_bt will become 0

    done= False             # bool of work is completed or not
    t=0                     # to keep record of time elapsed

    while(not done):
        done= True
        for i in range(0,n):

            if rem_bt[i]>0:
                done=False            #if remaining_burstTime is not zero then it means that work is not fully done

                if rem_bt[i]>q:
                    rem_bt[i]-=q         #remaining time is decreased by q time
                    t+=q             #time elapsed is increased by q quantum numvbers
                
                else:               #if remaining time is <=q
                    t+=rem_bt[i] 
                    rem_bt[i]=0
                    
                    wt[i]=t-bt[i]   #time elapsed - time required bt process to get done will result in standby time of particular process
        

def find_turn_around_time(bt,wt,tat,n):

    for i in range(n):
        tat[i]=wt[i]+bt[i]



def find_average_time(process,bt,n,q):
    tat=[0]*n
    wt=[0]*n
    total_tat=0
    total_wt=0

    find_waiting_time(wt,bt,n,q)

    find_turn_around_time(bt,wt,tat,n)

    for x,y in zip(tat,wt):
        total_tat+=x
        total_wt+=y

    print("Average waiting time is", total_wt/n)
    print("Average turn around  time is", total_tat/n)

if __name__=='__main__':
    process=[1,2,3,4,5]
    burst_time=[5,3,1,2,3]
    n=5
    time_quantum=2

    find_average_time(process,burst_time,n,time_quantum)