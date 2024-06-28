#define M(X,Y)(X>Y?X:Y)
#define D double
#define F f[i]
#define I -F[1]/(2*F[0])
c(void*a,void*b){return*((D*)b+3)-*((D*)a+3);}D e(D x,D*r){return x*x*r[0]+x*r[1]+r[2];}main(n,i,j){D f[100000][4],r=0;scanf("%d",&n);for(i=0;i<n;i++)scanf("%lf%lf%lf%lf",F,F+1,F+2,F+3);qsort(f,n,32,c);for(i=1;i<n;i++)for(j=0;j<3;j++)F[j]+=f[i-1][j];for(i=0;i<n;i++)r=M(r,M(F[2],M(e(M((I<F[3]?I:0),0),F),e(F[3],F))));printf("%lf",r);}