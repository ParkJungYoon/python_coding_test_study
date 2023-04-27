package javacodingtest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ11055 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder sb = new StringBuilder();
    private static StringTokenizer st;

    private static int n;
    private static int[] a;
    private static int[] dp;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        dp = a.clone();
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (a[i] > a[j]) {
                    if (dp[j] + a[i] > dp[i]) {
                        dp[i] = dp[j] + a[i];
                    }
                }
            }
        }

        int max = 0;
        for (int d : dp) {
            if (d > max) {
                max = d;
            }
        }
        System.out.println(max);
    }
}
