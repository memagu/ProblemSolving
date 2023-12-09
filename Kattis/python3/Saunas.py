i=input
v=sorted(list(map(int,i().split()))[::-1]for _ in range(int(i())))
_,c,b,a=map(sum,zip(*v))
r=0
for t,f,e,d in v:r=max(r,*(a*x*x+b*x+c for x in(0,-b/(2*a+1e-9),t)if 0<=x<=t));a-=d;b-=e;c-=f
print(r)