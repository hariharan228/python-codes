import java.util.*;

class Mincost {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();

            int[][] matrix = new int[n][m];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    matrix[i][j] = scanner.nextInt();
                }
            }

            Map<String, Integer> lookup = new HashMap<>();
            int result = minWays(matrix, 0, 0, lookup);
            System.out.println(result);
        }
    }

    public static int minWays(int[][] matrix, int i, int j, Map<String, Integer> lookup) {
        int n = matrix.length;
        int m = matrix[0].length;

        String key = i + "," + j;
        if (lookup.containsKey(key)) {
            return lookup.get(key);
        }

        if (i == n - 1 && j == m - 1) {
            lookup.put(key, matrix[i][j]);
            return matrix[i][j];
        } else if (i == n - 1) {
            int min = matrix[i][j] + minWays(matrix, i, j + 1, lookup);
            lookup.put(key, min);
            return min;
        } else if (j == m - 1) {
            int min = matrix[i][j] + minWays(matrix, i + 1, j, lookup);
            lookup.put(key, min);
            return min;
        } else {
            int min = matrix[i][j] + Math.min(minWays(matrix, i + 1, j, lookup), minWays(matrix, i, j + 1, lookup));
            lookup.put(key, min);
            return min;
        }
    }
}
