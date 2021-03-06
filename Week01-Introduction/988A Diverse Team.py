#DECLARING VARIABLES
memberNow=0         #SHOWING HOW MANY MEMBER IS IN THE TEAM NOW
sameRank=False      #BOOLEAN TO SHOW IF THE RANK IS IN THE TEAM OR NOT
teamMember=[]       #THE NUMBER OF THE STUDENTS IN THE TEAM
#INPUT TOTAL STUDENTS AND NUMBER OF STUDENT(S) IN A TEAM
studentNum, teamCons = map(int, input().split())
#INPUT ALL STUDENTS RANK
allRanks = [int(x) for x in input().split()]
#CHECK ALL OF THE STUDENT RANKS
for i in range(studentNum):
    #THE FIRST ONE IS ALWAYS HAVE DIFFERENT RANK BECAUSE, THERE IS NO ONE IN THE TEAM
    if (i==0):
        #ADD THE STUDENT NUMBER TO ARRAY AND TEAM MEMBER
        teamMember.append(i+1)
        memberNow=memberNow+1
    else:
        #IF THE REQUIRED STUDENT(S) IN THE TEAM IS REACHED
        if (memberNow==teamCons):
            break
        #CHECK WHETHER THE RANK IS THE SAME WITH THE OTHERS
        for j in range(i):
            if (allRanks[i]==allRanks[j]):
                sameRank=True
                break
        #IF THE RANK IS DIFFERENT FROM THE REST OF THE TEAM
        if (sameRank==False):
            #ADD THE STUDENT NUMBER TO ARRAY AND TEAM MEMBER
            teamMember.append(i+1)
            memberNow=memberNow+1
        #IF IT IS THE SAME, RESET sameRank TO FALSE
        else:
            sameRank=False
#IF THE MEMBER REACH THE REQUIRED OF EACH TEAM
if (memberNow>=teamCons):
    print("YES")
    print(" ".join(str(student) for student in teamMember))
#OTHERWISE "NO"
else:
    print("NO")
