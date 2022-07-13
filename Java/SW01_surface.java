// 22 하계 대학생 S/W 알고리즘 특강 사전문제 1번 해수면.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.Arrays;

import java.io.FileInputStream;

class SW01_surface
{
	static int T, N;
	static int[][] graph;
	static boolean[][] visit;
	static int count;
	static int[] dx = { 0, -1, 0, 1 };
	static int[] dy = { 1, 0, -1, 0 };

	static void bfs(int X, int N, int x, int y) {
		Queue<int[]> qu = new LinkedList<int[]>();
		qu.add(new int[] { x, y });

		while (!qu.isEmpty()) {
			x = qu.peek()[0];
			y = qu.peek()[1];

			visit[x][y] = true;
			qu.poll();

			for (int i = 0; i < 4; i++) {
				int cx = x + dx[i];
				int cy = y + dy[i];

				if (cx >= 0 && cy >= 0 && cx < N && cy < N) {
					if (!visit[cx][cy] && graph[cx][cy] > X) {
						qu.add(new int[] { cx, cy });
						visit[cx][cy] = true;
					}
				}

			}

		}
	}
	public static void main(String args[]) throws IOException
	{
		// System.setIn(new FileInputStream("C:\\Users\\user\\Desktop\\개발바닥\\CS\\Java\\Hello\\src\\input.txt"));

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{        
			StringTokenizer st = new StringTokenizer(br.readLine());         
			int N = Integer.parseInt(st.nextToken());        

			graph = new int[N][N];
			visit = new boolean[N][N];

			for (int i = 0; i < N; i++) {            
				st = new StringTokenizer(br.readLine());            
				for (int j = 0; j < N; j++) {                
					graph[i][j] = Integer.parseInt(st.nextToken());    
				}        
			}

			int max_result = 0;
			int X = 0;
			while(true) {
				count = 0; 

				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						if (graph[i][j] > X && !visit[i][j]) {
							bfs(X, N, i, j);
							count++;
						}
					}
				}

				X++;
				if (count == 0) {
					break;
				}
	
				if (count > max_result) {
					max_result = count;
				}
			
				// 초기화
				for(int xx = 0; xx < N; xx++) {
					Arrays.fill(visit[xx], false);
				}
			}

			System.out.println("#" + test_case + " " + max_result);
	}
  }
}