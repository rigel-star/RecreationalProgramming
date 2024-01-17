using System.Security.Cryptography.X509Certificates;

namespace Chess {
    public class NQueenPuzzle {
        public static void PrintGrid(int[,] grid) {
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    Console.Write(grid[i, j] + "    ");
                }
                Console.WriteLine();
            }
        }

        public static bool Solve(int[,] grid, int col) {
            if (col >= 8) return true;
            for (int i = 0; i < 8; i++) {
                if (CheckRow(grid, i) && CheckCol(grid, col) && CheckDiag(grid, i, col)) {
                    grid[i, col] = 1;
                    if (Solve(grid, col + 1)) return true;
                    grid[i, col] = 0;
                }
            }
            return false;
        }
        
        private static bool CheckRow(int[,] grid, int row) {
            for (int col = 0; col < 8; col++) {
                if (grid[row, col] == 1) return false;
            }
            return true;
        }
        
        private static bool CheckCol(int[,] grid, int col) {
            for (int row = 0; row < 8; row++) {
                if (grid[row, col] == 1) return false;
            }
            return true;
        }
        
        private static bool CheckDiag(int[,] grid, int row, int col) {
            for (int x = row+1, y = col+1; InRange(x, y); x++, y++) {
                if (grid[x, y] == 1) return false;
            }
            for (int x = row-1, y = col-1; InRange(x, y); x--, y--) {
                if (grid[x, y] == 1) return false;
            }
            for (int x = row-1, y = col+1; InRange(x, y); x--, y++) {
                if (grid[x, y] == 1) return false;
            }
            for (int x = row+1, y = col-1; InRange(x, y); x++, y--) {
                if (grid[x, y] == 1) return false;
            }
            return true;
        }

        private static bool InRange(int row, int col) {
            return row >= 0 && row < 8 && col >= 0 && col < 8;
        }
    }
}