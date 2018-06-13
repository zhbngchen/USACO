/*
ID: zhbngch1
PROG: ariprog
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
    ofstream fout ("ariprog.out");
    ifstream fin ("ariprog.in");
    int N, M;
    fin >> N;
    fin >> M;
    //cout << "N=" << N << endl;
    //cout << "M=" << M << endl;

    int sizeBisquares = M*M*2 + 1;
    int *bisquares = new int[sizeBisquares];
    for (int i = 0; i < sizeBisquares; i++)
    {
      bisquares[i] = 0;
    }

    //cout << "sizeBisquares=" << sizeBisquares << endl;
    for (int i = 0; i <= M; i++)
      for (int j = 0; j <= M; j++)
      {
        int index = i*i + j*j;
        //cout << "index=" << index << " i=" << i << " j=" << j << endl;
        bisquares[index] = 1;
      }
    /*cout << "bisquares: ";
    for (int i = 0; i < sizeBisquares; i++)
      cout << bisquares[i];
    cout << endl;
    */
    int maxB = M*M*2/(N-1);
    int maxA = M*M*2 - N;

    vector<pair<int, int> > results;

    for (int i = 0; i < sizeBisquares; i++)
    {
      if (bisquares[i] != 0)
      {
        for (int j = 1; j <= maxB; j++)
        {
          bool found = true;
          if ((i+j*(N-1)) >= sizeBisquares)
          {
            found = false;
            break;
          }
          for (int k = 0; k < N; k++)
          {
            //cout << "i=" << i << " j=" << j << " k=" << k << " i+j*k=" << (i+j*k) << " bisquare=" << bisquares[i+j*k] << endl;
            if (bisquares[i+j*k] == 0)
            {
              found = false;
              break;
            }
          }
          if (found == true)
          {
            pair<int, int> p(j, i);
            results.push_back(p);
          }
        }
      }
    }

    sort(results.begin(), results.end());

    for (int i = 0; i < results.size(); i++)
    {
      fout << results.at(i).second << ' ' << results.at(i).first << endl;
    }
    if (results.size() == 0)
      fout << "NONE" << endl;
    return 0;
}

