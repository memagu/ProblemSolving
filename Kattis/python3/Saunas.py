i=input
v=sorted([*map(int,i().split())][::-1]for _ in[0]*int(i()))
_,c,b,a=map(sum,zip(*v))
r=0
for t,f,e,d in v:r=max(r,c,*(a*x*x+b*x+c for x in(-b/(2*a+.01),t)if 0<x<=t));a-=d;b-=e;c-=f
print(r)