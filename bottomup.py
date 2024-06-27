#botton-up approach(iterative[tabulation])
    

p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
c=15
n=len(p)#len(w)
DP=[[0 for i in range(c+1)] for j in range(n+1)]
for i in range(1,n+1):
     for j in range(1,c+1):
            if j-w[i-1]<0:
                DP[i][j]=DP[i-1][j]
            else:
                DP[i][j]=max(DP[i-1][j],p[i-1]+DP[i-1][j-w[i-1]])
            

print(DP[n][c])
