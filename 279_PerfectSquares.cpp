class Solution {
public:
    int numSquares(int n) {
        int dp[101][10001] = {0};
        int tmp = 0,i=1;
        
        for(int i = 1;i<10001;i++){
            dp[1][i]=i;
        }
        
        for(i = 2;i*i <= n;i++){
            tmp = i*i;
            for(int j=1;j<=n;j++){
                if(j < tmp){
                    dp[i][j] = dp[i-1][j];
                }else{
                    int r = j - tmp;
                    dp[i][j] = min(dp[i][r]+1, dp[i-1][j]);
                }
            }
        }
       
        return dp[i-1][n];
    }
};