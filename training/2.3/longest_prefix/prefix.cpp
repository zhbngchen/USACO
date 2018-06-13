/* 
ID: zhbngch1
PROG: prefix 
LANG: C++ 
*/  
#include<iostream>  
#include<cstring>  
#include<cstdio>  
#include<algorithm>  
#include<queue>  
#define mp make_pair  
using namespace std;  
typedef long long lng;  
int n;  
string list[201],s,pre,t;  
bool dp[222222];  
bool f()  
{  
    for(int i=0;i<n;++i)  
    if(pre==list[i]) return 1;  
    return 0;  
}  
int main()  
{  
  #ifndef  DEBUG  
  freopen("prefix.in","r",stdin);  
  freopen("prefix.out","w",stdout);  
  #endif  
  while(1)  
  {  
      cin>>list[n];  
      if(list[n]==".") break;  
      n++;  
  }  
  while(cin>>t){s+=t;}  
  dp[0]=1;  
  for(int i=1,z=s.size();i<=z;++i)  
  {  
      for(int j=1;j<=10&&j<=i;++j)  
     if(dp[i-j]) {pre=s.substr(i-j,j);  
      if(f()) {dp[i]=1;break;}  
      }  
  }  
  int ans;  
  for(ans=s.size();;--ans)  
  if(dp[ans]) break;  
  printf("%d\n",ans);  
    return 0;  
}  
