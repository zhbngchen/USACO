"""
PROG: nocows
LANG: PYTHON3

"""
import sys

"""
numNodes levelTree  numTrees
1	        1	          1		O							  	T1

3	        2	          1	 	O							  	T1
		         	           / \  						   / \
 		                      O   O		   					  T1 T1

5	        3	          2		  O		        O					       T1	    T1
			                     / \	       / \					      / \      / \
			                    O   O   	  O   O				         T3  T1   T1  T3
			                   / \	             / \
              			      O   O	            O   O

7	        3	          1	 	 O							T1
			                   /  \						   / \
			                  O    O					  T3 T3
			                 / \  / \
			                O   O O  O

	        4	          4		O		    O		    O		    O		    T1(2)	T1(2)
			                   / \	       / \	       / \	       / \ 	       / \     / \
			                  O   O	      O   O	      O   O	      O   O	      T5 T1   T1  T5
            			     / \	     / \ 	         / \	     / \
            			    O   O	    O   O		    O   O		O   O
            			   / \		       / \	       / \		       / \
            			  O   O		      O   O	      O   O		      O   O

9	        4	          6				
                              						T1(2)  T1(2)	T1	   T1
											       / \     / \     / \     / \
											      T3 T5   T5 T3   T1 T7   T7 T1  (T7 with numTree 3)

	        5	          8			 				T1(4)	T1(4)
											       / \     / \
											      T1  T7  T7 T1  (T7 with numTree 4)

numTrees
---------------------------------------------------------------------------
 j/levelTree		0	  1	  2	  3	  4	  5	  6
		0	


		1		            1

		2

		3			              1

		4

i/numNodes 	5				        2

		6

		7				                1	  4

		8

		9					                  6	  8
---------------------------------------------------------------------------
				| |  In order to be able to calculate numTrees[levelTrees] based on numTrees[levelTrees-1], 
				V V  add numTrees[i][j] into numTrees[i][j+1]. And the final result will be numTrees[n][k] - numTrees[n][k-1]
numTrees
---------------------------------------------------------------------------
j/levelTree		0	  1	  2	  3	  4	  5	  6
		0	

		1		          1	  1	  1	  1	  1	  1

		2

		3		    	        1	  1	  1	  1	  1

		4

i/numNodes	5				      2	  2	  2	  2

		6

		7				              1	  5	  5	  5
	
		8

		9					                6	  14	14
---------------------------------------------------------------------------


"""

def print2d(dp):
  for d in dp:
    print(d)

with open("nocows.in", "r") as fin:
  lines = fin.readlines()

N, K = map(int, lines[0].split())
print(N, K)

dp = []
for _ in range(N+1):
  dp.append([0] * (K+1))

for j in range(1, K+1):
  dp[1][j] = 1
print("after init:")
print2d(dp)

for i in range(3, N+1, 2):
  for j in range(2, K+1):
    if dp[i][j-1] != 0 and dp[i][j-1] == dp[i][j-2]:
      dp[i][j] = dp[i][j-1]
    else:
      sumCounts = 0
      for k in range(1, i, 2):
        sumCounts += dp[k][j-1] * dp[i-1-k][j-1]
      dp[i][j] = sumCounts % 9901
print("after calculations, dp:")
print2d(dp)

with open('nocows.out', 'w') as fout:
  fout.write(str(((dp[N][K] - dp[N][K-1]) + 9901)%9901) + '\n')

