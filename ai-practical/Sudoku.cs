using Chess;

namespace Sudoku {
    public class Program {
        // for sudoku
        static void Main(string[] args) {
            int[,] grid = {
                {-1, 4, -1, -1, -1, -1, -1, -1, -1},
                {-1, -1, -1, -1, -1, -1, -1, -1, -1},
                {-1, -1, -1, -1, -1, -1, -1, -1, -1},
                {-1, -1, -1, -1, -1, -1, -1, -1, -1},
                {-1, -1, -1, -1, -1, -1, -1, -1, -1},
                {-1, -1, -1, -1, -1, -1, -1, -1, -1},
                {-1, -1, -1, -1, -1, -1, -1, -1, -1},
                {-1, -1, -1, -1, -1, -1, -1, -1, -1},
                {-1, -1, -1, -1, -1, -1, -1, -1, -1},
            };
            if(Solve(grid)) {
                PrintGrid(grid);
            }
        }
        
        /*
        // for n-queens puzzle problem
        static void Main3(string[] args) {
            int[,] grid = {
                {0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0}
            };
            if (Chess.NQueenPuzzle.Solve(grid, 0)) Chess.NQueenPuzzle.PrintGrid(grid);
        }

        // for eight puzzle problem
        static void Main4(string[] args) {
            int[,] grid = {
                {7, 4, 2},
                {5, -1, 1},
                {8, 3, 6}
            };
            int[,] goal = {
                {-1, 1, 2},
                {3, 4, 5},
                {6, 7, 8}
            };
            EightPuzzleProblem.EightPuzzleProblem.Solve(grid, goal);
        }

        // for a-star problem
        static void Main(string[] args) {
            int[,] grid = {
                {2, 1, 1, 1, 1, -1, -1},
                {1, 1, -1, -1, 1, 1, -1},
                {1, -1, 1, 1, 1, -1, -1},
                {-1, 1, 1, 1, 1, 1, -1},
                {1, -1, 1, -1, 1, 1, 3}
            };
            AStar.AStar.Solve(grid);
        }
        */

        static void PrintGrid(int[,] grid) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    Console.Write(grid[i, j] + "    ");
                }
                Console.WriteLine();
            }
        }

        static bool Solve(int[,] grid) {
            (int, int) cell = FindEmptyCell(grid);
            if (cell.Item1 == -1 || cell.Item2 == -1) {
                return true;
            }
            int row = cell.Item1, col = cell.Item2;
            for (int num = 1; num <= 9; num++) {
                if (RowCheck(grid, row, num) && 
                    ColumnCheck(grid, col, num) && 
                    BoxCheck(grid, row, col, num)) {
                        grid[row, col] = num;
                        if (Solve(grid)) return true;
                        grid[row, col] = -1;
                }
            }
            return false;
        }

        static (int, int) FindEmptyCell(int[,] grid) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    if (grid[i, j] == -1) return (i, j);
                }
            }
            return (-1, -1);
        }

        static bool RowCheck(int[,] grid, int row, int num) {
            for (int col = 0; col < 9; col++) {
                if(grid[row, col] == num) return false;
            }
            return true;
        }

        static bool ColumnCheck(int [,] grid, int col, int num) {
            for (int row = 0; row < 9; row++) {
                if (grid[row, col] == num) return false;
            }
            return true;
        }

        static bool BoxCheck(int [,] grid, int i, int j, int num) {
            int row = (i / 3) * 3 + 1;
            int col = (j / 3) * 3 + 1;
            for (int ir = -1; ir < 2; ir++) {
                for (int jc = -1; jc < 2; jc++) {
                    if (grid[row + ir, col + jc] == num) return false;
                }
            }
            return true;
        }
    }
}
