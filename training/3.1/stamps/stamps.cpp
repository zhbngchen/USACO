/*
ID: zhbngch1
PROG: stamps
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

#define ARRAYSIZE 2000020

int main() {
    int results[ARRAYSIZE];
    for (int i = 0; i < ARRAYSIZE; i++)
    {
        results[i] = 0;
    }

    ofstream fout ("stamps.out");
    ifstream fin ("stamps.in");
    int K, N;
    fin >> K;
    fin >> N;
    vector<int> numbers;
    for (int i = 0; i < N; i++)
    {
        int val;
        fin >> val;
        numbers.push_back(val);
    }

    sort(numbers.begin(), numbers.end(), greater<int>());
    /* for (auto number: numbers)
    {
        cout << number << ' ';
    }
    cout << endl;*/

    for (int i = 1; ; i++)
    {
        for (auto number : numbers)
        {
            if (i - number >= 0)
            {
                if (results[i] == 0 || results[i] > results[i-number] + 1)
                {
                    results[i] = results[i-number] + 1;
                }
            }
        }
        if (results[i] == 0 || results[i] > K)
        {
            fout << i-1 << endl;
            return 0;
        }
    }

    return 0;
}