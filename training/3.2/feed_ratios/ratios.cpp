/*
PROG: ratios
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
    ifstream fin("ratios.in");
    ofstream fout("ratios.out");

    int target[3];
    fin >> target[0] >> target[1] >> target[2];

    int inputs[3][3];
    for (int i = 0; i < 3; ++i)
    {
        fin >> inputs[i][0] >> inputs[i][1] >> inputs[i][2];
    }

    for (int i = 0; i < 100; ++i)
        for (int j = 0; j < 100; ++j)
            for (int k = 0; k < 100; ++k)
            {
                int combos[3], factor = 0;
                for (int l = 0; l < 3; ++l)
                {
                    combos[l] = i * inputs[0][l] + j * inputs[1][l] + k * inputs[2][l];
                    if (target[l] != 0)
                        factor = combos[l]/target[l] > factor ? combos[l]/target[l] : factor;
                }
                
                if (factor != 0 && factor*target[0] == combos[0] && factor*target[1] == combos[1] && factor*target[2] == combos[2])
                {
                    fout << i << ' ' << j << ' ' << k << ' ' << factor << endl;
                    return 0;
                }
            }
    fout << "NONE" << endl;

    return 0;
}