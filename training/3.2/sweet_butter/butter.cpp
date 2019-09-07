/*
PROG: butter
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

#define MYMAX (1 << 30)
#define PASTURES 800
#define COWS 500

struct Edge {
    int pasture;
    int distance;
    Edge(int p, int d) : pasture(p), distance(d) {}
};

int d[PASTURES][PASTURES];
int pastures[COWS];
vector<Edge> edges[PASTURES];

void spfa(int u, int P, const vector<Edge> edges[PASTURES], int d[PASTURES][PASTURES])
{
    queue<int> q;
    q.push(u);
    bool visited[PASTURES];
    //cout << "u=" << u << endl;
    for (int i = 0; i < P; i++)
        visited[i] = false;
    while(!q.empty())
    {
        int cur = q.front();
        //cout << "cur=" << cur << endl;
        q.pop();
        for (int i = 0; i < edges[cur].size(); ++i)
        {
            int v = edges[cur][i].pasture;
            int distance = edges[cur][i].distance;
            //if (cur == 3 && v == 6)
                //cout << "d[0][6]=" << d[0][6] << ", d[0][3]=" << d[0][3] << ", w[3][6]=" << w[3][6] << ", visited[6]=" << visited[6] << endl;
            if (d[u][v] > d[u][cur] + distance)
            {
                d[u][v] = d[u][cur] + distance;

                if (visited[v] == false)
                {
                    q.push(v);
                    //cout << "pushing=" << v << endl;
                    visited[v] = true;
                }
            }
        }
        visited[cur] = false;
    }
}

int main()
{
    ifstream fin("butter.in");
    ofstream fout("butter.out");

    int N, P, C;
    fin >> N >> P >> C;

    for (int i = 0; i < N; ++i)
    {
        fin >> pastures[i];
        pastures[i] -= 1;
    }

    for (int i = 0; i < P; ++i)
        for (int j = 0; j < P; ++j)
        {
            d[i][j] = MYMAX;
        }

    for (int i = 0; i < C; ++i)
    {
        int start, end, size;
        fin >> start >> end >> size;
        
        edges[start-1].push_back(Edge(end-1, size));
        edges[end-1].push_back(Edge(start-1, size));
    }

    for (int i = 0; i < P; ++i)
    {
        d[i][i] = 0;
    }

    for (int i=0; i < P; ++i)
    {
        spfa(i, P, edges, d);
    }
    int result = MYMAX;
    for (int i = 0; i < P; ++i)
    {
        int totalLen = 0;
        for (int j = 0; j < N; ++j)
            totalLen += d[i][pastures[j]];
        if (result > totalLen)
        {
            result = totalLen;
            //cout << "i=" << i << endl;
        }
    }

    fout << result << endl;
}