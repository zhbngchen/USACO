/*
ID: zhbngch1
PROG: pprime
LANG: C++
*/
//#pragma comment(linker, "/STACK:16777216") //for c++ Compiler
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <stack>
#include <string>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <vector>
#include <algorithm>
#define Max(a,b) (((a) > (b)) ? (a) : (b))
#define Min(a,b) (((a) < (b)) ? (a) : (b))
#define Abs(x) (((x) > 0) ? (x) : (-(x)))
#define MOD 1000000007
#define pi acos(-1.0)

using namespace std;

typedef long long           ll      ;
typedef unsigned long long  ull     ;
typedef unsigned int        uint    ;
typedef unsigned char       uchar   ;

template<class T> inline void checkmin(T &a,T b){if(a>b) a=b;}
template<class T> inline void checkmax(T &a,T b){if(a<b) a=b;}

const double eps = 1e-7      ;
const int M = 660000         ;
const ll P = 10000000097ll   ;
const int INF = 0x3f3f3f3f   ;
const int MAX_N = 20         ;
const int MAXSIZE = 101000000;

bool primei(int n){
    int i, j;
    for(i = 2; i <= sqrt(n); ++i){
        if(n % i == 0)  return false;
    }
    return true;
}

ll b[10000]={5,7,11};
int p[8]={4,2,4,2,4,6,2,6};
bool prime(int n){
    int i = 7, j, q;
    if(n == 1)  return false;
    if(n == 2 || n == 5 || n == 3)  return true;
    if(n % 2 == 0 || n % 3 == 0 || n % 5 == 0)  return false;
    q = (int)sqrt((double)n);
    for(; i <= q; ){
        for(j = 0; j < 8; ++j){
            if(n % i == 0)  return false;
            i += p[j];
        }
        if(n % i == 0)  return false;
    }
    return true;
}
int creat(){
    int i, j, k, l, m, count = 3;
    for(i = 1; i <= 9; i += 2)
        for(j = 0; j <= 9; ++j)
            b[count++] = 100 * i + 10 * j + i;
    for(i = 1; i <= 9; i += 2)
        for(j = 0; j <= 9; ++j)
            for(k = 0; k <= 9; ++k)
              b[count++] = 10000 * i + 1000 * j + k * 100 + j * 10 + i;
        for(i = 1; i <= 9; i += 2)
         for(j = 0; j <= 9; ++j)
            for(k = 0; k <= 9; ++k)
                for(l = 0; l <= 9; ++l)
                  b[count++] = 1000000 * i + 100000 * j + k * 10000 + l * 1000 + k * 100 + j * 10 + i;
        return count - 1;
}

int main() {
    ofstream fout ("pprime.out");
    ifstream fin ("pprime.in");
    int i, j, k, t, n, s, c, w, q;
    int a;
    n = creat();
    fin >> a >> c;
    for(i = 0; i < n; ++i){
        if(b[i] >= a){
            if(b[i] > c) break;
            if(prime(b[i])){
                fout << b[i] << endl;
            }
        }
    }

    fin.close();
    fout.close();
    return 0;
}

