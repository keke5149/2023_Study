class Solution {
    static int [] dx = {1, -1, 0, 0};
	static int [] dy = {0, 0, 1, -1};
	static int count = 0;
	
	public static void check(int [][] pictures, int x, int y, int m, int n, int [][] visited) {
		
		if(visited[x][y] == 1) return;
		
		visited[x][y] = 1;
		count++;
		
		int tx=0, ty=0;
		for(int i = 0; i <= 3; i++) {
			tx = x + dx[i];
			ty = y + dy[i];
			if((tx >= 0 && tx < m) && (ty >= 0 && ty < n)) {
				if(pictures[x][y] == pictures[tx][ty] && visited[tx][ty] == 0) {
					check(pictures, tx, ty, m, n, visited);
				}
			}
		}
	}
    
    public static int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        int [][] visited = new int[m][n];
        for(int i = 0; i < m; i++) {
        	for(int j = 0; j < n; j++) {
        		if(picture[i][j] != 0 && visited[i][j] == 0) {
        			numberOfArea++;
        			check(picture, i, j, m, n, visited);
        		}
        		//한 영역 전부 확인 끝
        		if(count > maxSizeOfOneArea) maxSizeOfOneArea = count;
        		count = 0;
        	}
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }

    public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] arr = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
		int [] answer = solution(6, 4, arr);
        System.out.println(answer[0]);
        System.out.println(answer[1]);
	}

}