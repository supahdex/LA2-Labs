%test
full(tomomap(2,2,45,sqrt(2)));

%task 1,1
T=full(tomomap(2,2,[0,90],1));
x=[4,6,3,1];
b=T*x
x=[0,1,1,0];
b=T*x
%task 1,2
full(tomomap(2,4,45,sqrt(2)/2));

%task 1,3
full(tomomap(4,2,[0,45],sqrt(2)));
