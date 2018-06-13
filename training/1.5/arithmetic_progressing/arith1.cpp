/*
ID: zhbngch1
PROG: ariprog
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void searchResult(int N, int indLists, int* lists[], int* sizeLists, int *cand, int sizeBisquares, int* bisquares,
    vector<int>& results)
{
  if (indLists == 2)
  {
    bool found = true;
    for (int i = 0; i < N; i ++)
    {
      int sumCand = cand[1] + i * cand[0];
      if ((sumCand >= sizeBisquares) || (bisquares[sumCand] == 0))
      {
        found = false;
        if (cand[0] ==4 && cand[1] == 37)
          //cout << "sumCand=" << sumCand << " bisquares[]=" << bisquares[sumCand] << endl;
        break;
      }
    }
    if (found)
    {
      results.push_back(cand[1]);
      results.push_back(cand[0]);
      //cout << "push_back " << cand[1] << " and " << cand[0] << endl;
    }
    return;
  }

  for (int i = 0; i < sizeLists[indLists]; i++)
  {
    cand[indLists] = lists[indLists][i];
    searchResult(N, indLists+1, lists, sizeLists, cand, sizeBisquares, bisquares, results);
  }
}

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
    int sizeLists[2];
    int *lists[2];
    lists[0] = new int[maxB];
    sizeLists[0] = maxB;
    lists[1] = new int[maxA + 1];
    sizeLists[1] = maxA + 1;
    for (int i = 1; i <= maxB; i++)
      lists[0][i-1] = i;
    for (int i = 0; i <= maxA; i++)
      lists[1][i] = i;

    int cand[2];
    vector<int> results;

    searchResult(N, 0, lists, sizeLists, cand, sizeBisquares, bisquares, results);

    for (int i = 0; i < results.size(); i++)
    {
      if ((i%2) == 1)
        fout << results.at(i) << endl;
      else
        fout << results.at(i) << ' ';
    }
    if (results.size() == 0)
      fout << "NONE" << endl;
    return 0;
}

