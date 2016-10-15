import numpy as np
avaResour = np.array([3,3,2])
allocation = np.array([[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]])
maxRequest = np.array([[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]])
need = np.array([[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]])
askResource=np.array([0,0,0])
def BankerAllgorithm():
    global avaResour,allocation,maxRequest,need,askResource
    print "thread num 5,res num 3"
    print "res available :"
    for x in avaResour:
        print x
    print("the max request :")
    for x in maxRequest:
        print x
    print "allocation :"
    for  x in allocation:
        print x
    print "need :"
    for x in need:
        print x    

    RequestThreadNum = input("enter the request thread number :from 0 -> 4 : ")
    #test RequestThreadNum is ok
    while RequestThreadNum>4 or RequestThreadNum<0:
        print("please enter the correct number ! From 0 - 4 : ")
        RequestThreadNum = input("enter the number : ")
   
   #input
    print "please enter  number of resources,the format is  x x x : "
    for x in xrange(0,3):
        askResource[x] = input()

    if askResource[x]<=need[RequestThreadNum][x]:
        print("Bankalgorithm is running ...biubiubiu...waiting...")
        if askResource[x]<=avaResour[x]:
            avaResour =avaResour - askResource
            allocation = allocation + askResource
            need[RequestThreadNum] = need[RequestThreadNum] - askResource
            print "Trial allocation is ok !"
            if (safeTest()):
                print "begin to allocation res to "+RequestThreadNum 
                print "allocation is ok,res has been refreshed"
                for x in xrange(0,5):
                    if  need[x]==0:
                        for y in xrange(0,3):
                            avaResour[y] = avaResour[y] + allocation[x][y]
                            allocation[x][y] = 0                                
            else:
                print "Trial allocation is wrong ,we are trying to get back to last statue!"
                avaResour = avaResour + askResource
                allocation = allocation - askResource
                need = need +askResource
        else:
            print "there is not enough resource now , try to wait for sometime!"
    else:
        print "error ! askResource is bigger than need"


def safeTest():       
    global avaResour,allocation,maxRequest,need,askResource
    s=0;m=0;z=0;r=[0,0,0,0,0];y=0;work=[0,0,0];finish = [0,0,0,0,0]
    print "enter safety test ..."
    work = avaResour
    for x in xrange(0,5):
        for y in xrange(0,5):
            if finish[y]==0 and need[y][0]<=work[0] and need[y][1]<=work[1] and need[y][2]<=work[2]:
                for z in xrange(0,3):
                    work[z] = work[z] + allocation[y][z]
                finish[y] =1;r[y] =s;
                y +=y

    if y==5:
        print "find a safety order"
        for x in xrange(0,3):
            print "P " +r[2*x]+"-->"+" P "+r[2*x +1]+"-->"
        print " P "+ r[4] +" pass safety test"
        return 1
    else:
        return 0
        
if __name__ == '__main__':
    BankerAllgorithm()
