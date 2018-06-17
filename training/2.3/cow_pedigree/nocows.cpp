#include <iostream>
using namespace std;

int dp[210][110];

int main()

{

    int n,k;

    cin>>n>>k;

    int i,j,m;

    for(j=0;j<=k;j++)//??????

        dp[1][j]=1;

    for(j=2;j<=k;++j)

        for(i=2;i<=n;++i)
        {
            for(m=1;m<=i-1;++m)
            {
              cout << "i=" << i << " j=" << j << " m=" << m << " j-1=" << j-1 << " i-1-m=" << i-1-m << " dp[m][j-1]=" << dp[m][j-1] << " dp[i-1-m][j-1]=" << dp[i-1-m][j-1] << endl;
              dp[i][j]=(dp[i][j]+dp[m][j-1]*dp[i-1-m][j-1])%9901;//????
            }
            cout << "dp[i][j]=" << dp[i][j] << endl;
        }

    for (i=0; i < 11; i++)
    {
      for (j=0; j < 6; j++)
        cout << dp[i][j] << ' ';
      cout << endl;
    }
    cout<<(dp[n][k]-dp[n][k-1]+9901)%9901<<endl;

    return 0;

}

