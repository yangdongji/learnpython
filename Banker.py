import numpy as np
def BankerAllgorithm():
    avaResour = np.array([3,3,2])
    allocation = np.array([[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]])
    maxRequest = np.array([[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]])
    need = np.array([[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]])
    askResource=np.array([0,0,0])
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

    if askResource.all()<=need.all():
        print("Bankalgorithm is running ...biubiubiu...waiting...")
        if askResource.all()<=avaResour.all():
            avaResour =avaResour - askResource
            allocation = allocation + askResource
            need[RequestThreadNum] = need[RequestThreadNum] - askResource
            print "Trial allocation is ok !"
            if (safeTest()):
                pass
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
    pass


if __name__ == '__main__':
    BankerAllgorithm()
