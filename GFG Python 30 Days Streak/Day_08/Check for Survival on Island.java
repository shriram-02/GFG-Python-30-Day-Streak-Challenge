class Solution {
    public int minimumDays(int S, int N, int M) {
        // code here
        if (M > N)
        
            return - 1;
        if(S > 6 && (7 * M > 6 * N))
            return - 1;
            int total_food = S * M;
            return (total_food + N - 1) / N;
    }
}