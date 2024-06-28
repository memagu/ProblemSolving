#define M(X,Y)(X>Y?X:Y)
#define D double
#define F f[i]
#define S-F[1]/(2*F[0])
#define L for(i=0;i<n;i++)
c(void*a,void*b){return*((D*)b+3)-*((D*)a+3);}D e(D x,D*r){return x*x*r[0]+x*r[1]+r[2];}main(n,i,j){D f[100001][4],r=0;scanf("%d",&n);L scanf("%lf%lf%lf%lf",F,F+1,F+2,F+3);qsort(f,n,32,c);L for(j=0;j<3;j++)f[i+1][j]+=F[j],r=M(r,M(F[2],M(e(M((S<F[3]?S:0),0),F),e(F[3],F))));printf("%lf",r);}