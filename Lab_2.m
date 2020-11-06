%From Lab 1, Matrix A,B and C
M_A = [0 0 8 8; 0 0 8 8; 8 8 0 0; 8 8 0 0];
M_B = [0 8 0 8; 8 0 8 0; 0 8 0 8; 8 0 8 0];
M_C = [8 0 0 8; 0 8 8 0; 0 8 8 0; 8 0 0 8];

%test
full(tomomap(2,2,45,sqrt(2)));

%task 1,1 (named x and y for Task 2 below)
T = full(tomomap(2,2,[0,90],1));
x = [4; 6; 3; 1];
b = T*x
y =[0; 1; 1; 0];
b = T*y

%task 1,2
full(tomomap(2,4,45,sqrt(2)/2));

%task 1,3
full(tomomap(4,2,[0,45],sqrt(2)));

b_A = T*M_A
b_B = T*M_B
b_C = T*M_C

%task 2,1
i = 3*x
ii = 0.5*y
iii = i + ii

b_i = T*i
b_ii = T*ii
b_iii = T*iii












