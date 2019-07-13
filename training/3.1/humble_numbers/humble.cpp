/*
ID: zhbngch1
PROG: humble
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <limits>

using namespace std;

int main() {
    ofstream fout ("humble.out");
    ifstream fin ("humble.in");
    int K, N;
    fin >> K;
    fin >> N;
    vector<int> primes;
    for (int i = 0; i < K; i++)
    {
        int val;
        fin >> val;
        primes.push_back(val);
    }

    vector<int> results(N+1);
    results[0] = 1;

    vector<int> indexes(K);

    for (int i = 1; i < N+1; i++)
    {
        int minNext = numeric_limits<int>::max();
        int index = 0;
        for (int j = 0; j < K; j++)
        {
            while (results[indexes[j]] * primes[j] <= results[i-1])
                indexes[j] ++;
            if (minNext > results[indexes[j]] * primes[j])
            {
                index = j;
                minNext = results[indexes[j]] * primes[j];
            }
        }
        results[i] = minNext;
        indexes[index] ++;
    }

    fout << results[N] << endl;

    return 0;
}