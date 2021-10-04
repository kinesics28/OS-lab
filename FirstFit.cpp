#include <iostream>
#include <cstring> // for using memeset
using namespace std;

int main()
{
    int blockSize[10]={0};
    int processSize[10]={0};
    int bn;              // number of blocks - block number
    int pn;              // number of process - process number
    int flags[10] = {0}; // all elements of flags array will be 0
    int allocation[10] = {0};   // this will store in which block ith process is stored
    int externalFragmentation=0;
    /* for (int i = 0; i < 10; i++)
    {
        allocation[i] = -1;
        cout << allocation[i] << endl;
    } */
    memset(allocation, -1, sizeof(allocation)); // all elements of allocation array will be -1
    cout << "Enter the number of blocks ";
    cin >> bn;
    for (int i = 0; i < bn; i++)
    {
        cout << "Enter size of " << i + 1 << " block ";
        cin >> blockSize[i];
    }
    cout << "Enter the number of proccesses ";
    cin >> pn;

    for (int i = 0; i < pn; i++)
    {
        cout << "Entre size of " << i + 1 << " process ";
        cin >> processSize[i];
    }
    // memory allocation from here using first fit -->

    for (int i = 0; i < pn; i++) // for each process
    {
        for (int j = 0; j < bn; j++)  // find a block
        {
            if (flags[j] == 0 && blockSize[j] >= processSize[i])
            {
                allocation[i]=i+1;
                flags[j]=1;
                externalFragmentation+=(blockSize[j]-processSize[i]);
                break;
            }
        }
    }

    //display allocation details
    cout << "\nProcess No.\tProcess Size\tBlock no.\n";
    for (int i = 0; i < pn; i++)
    {
        cout << " " << i+1 << "\t\t"<< processSize[i] << "\t\t";
        if (allocation[i] != -1)
            cout << allocation[i]+1;
        else
            cout << "Not Allocated";
        cout << endl;
    }
    
    cout<<"Total external fragmentation is: "<<externalFragmentation;
   
    return 0;
}

// sample input-->
/*
5
100
500
200
300
600
4
212
417
112
426

*/

//sample output -->
/*

Process No.    Process Size    Block no.
   1               212            2
   2               417            5
   3               112            2
   4               426        Not Allocated
*/
