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
    bool operator<(const Edge& other) const
    {
        return distance > other.distance; // opposite > because top is biggest by default
    } 
};

int d[PASTURES][PASTURES];
int pastures[COWS];
vector<Edge> edges[PASTURES];

void dijkstra(int u, int P, const vector<Edge> edges[PASTURES], int d[PASTURES][PASTURES])
{
    priority_queue<Edge> q;
    q.push(Edge(u, 0));
    bool visited[PASTURES];
    //cout << "u=" << u << endl;
    for (int i = 0; i < P; i++)
        visited[i] = false;
    while(!q.empty())
    {
        Edge cur = q.top();
        //cout << "cur=" << cur << endl;
        q.pop();
        if (visited[cur.pasture] == true)
            continue;
        visited[cur.pasture] = true;
        for (int i = 0; i < edges[cur.pasture].size(); ++i)
        {
            int v = edges[cur.pasture][i].pasture;
            int distance = edges[cur.pasture][i].distance;
            //if (cur == 3 && v == 6)
                //cout << "d[0][6]=" << d[0][6] << ", d[0][3]=" << d[0][3] << ", w[3][6]=" << w[3][6] << ", visited[6]=" << visited[6] << endl;
            if (d[u][v] > d[u][cur.pasture] + distance)
            {
                d[u][v] = d[u][cur.pasture] + distance;

                if (visited[v] == false)
                {
                    q.push(Edge(v, d[u][v]));
                    //cout << "pushing=" << v << endl;
                }
            }
        }
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
        dijkstra(i, P, edges, d);
    }
    int result = MYMAX;
    for (int i = 0; i < P; ++i)
    {
        int totalLen = 0;
        for (int j = 0; j < N; ++j)
            totalLen += d[pastures[j]][i];
        if (result > totalLen)
        {
            result = totalLen;
            //cout << "i=" << i << endl;
        }
    }

    fout << result << endl;
}