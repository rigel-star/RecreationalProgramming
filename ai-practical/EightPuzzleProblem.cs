using System.Text;

namespace EightPuzzleProblem {
    public class EightPuzzleProblem {
        private static HashSet<string> visitedStates = new();

        public static bool Solve(int[,] grid, int[,] goal) {
            if (CompareToGoalState(grid, goal)) {
                Console.WriteLine("Goal state satisfied!");
                return true;
            }
            string currentState = GetStringRepresentation(grid);
            if (visitedStates.Contains(currentState)) {
                return false;
            }
            visitedStates.Add(currentState);
            (int, int) freeSlot = FindFreeSlot(grid);
            int fx = freeSlot.Item1;
            int fy = freeSlot.Item2;
            if (fx == -1 || fy == -1) return true;
            List<(int, int)> neighbors = GetNeighbors(grid, freeSlot.Item1, freeSlot.Item2);
            int cost = int.MaxValue;
            int sx = neighbors[0].Item1;
            int sy = neighbors[0].Item2;
            foreach ((int, int) neighbor in neighbors) {
                int nx = neighbor.Item1;
                int ny = neighbor.Item2;
                SwapCellValues(grid, nx, ny, fx, fy);
                int tmpCost = CalculateCost(grid, goal);
                if (tmpCost <= cost) {
                    cost = tmpCost;
                    sx = nx;
                    sy = ny;
                } else SwapCellValues(grid, nx, ny, fx, fy);
                PrintGrid(grid);
                if (Solve(grid, goal)) return true;
                SwapCellValues(grid, fx, fy, sx, sy);
            }
            return false;
        }

        private static void SwapCellValues(int[,] grid, int x1, int y1, int x2, int y2) {
            int fv = grid[x1, y1];
            int sv = grid[x2, y2];
            grid[x1, y1] = sv;
            grid[x2, y2] = fv;
        }

        private static int CalculateCost(int[,] grid, int[,] goal) {
            int result = 0;
            for (int x = 0; x < 3; x++) {
                for (int y = 0; y < 3; y++) {
                    if (grid[x, y] != goal[x, y]) result++;
                }
            }
            return result;
        }

        public static void PrintGrid(int[,] grid) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    Console.Write(grid[i, j] + "    ");
                }
                Console.WriteLine();
            }
            Console.WriteLine("\n");
        }

        private static (int, int) FindFreeSlot(int[,] grid) {
            for (int x = 0; x < 3; x++) {
                for (int y = 0; y < 3; y++) {
                    if (grid[x, y] == -1) return (x, y);
                }
            }
            return (-1, -1);
        }

        private static bool CompareToGoalState(int[,] grid, int[,] goal) {
            for (int x = 0; x < 3; x++) {
                for (int y = 0; y < 3; y++) {
                    if (grid[x, y] != goal[x, y]) return false;
                }
            }
            return true;
        }

        private static List<(int, int)> GetNeighbors(int[,] grid, int x, int y) {
            List<(int, int)> result = new();
            (int, int)[] neighborCoords = {
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
            };
            foreach((int, int) coords in neighborCoords) {
                int x1 = coords.Item1;
                int y1 = coords.Item2;
                if (x1 >= 0 && x1 < 3 && y1 >= 0 && y1 < 3) {
                    result.Add((x1, y1));
                }
            }
            return result;
        }

        private static string GetStringRepresentation(int[,] grid) {
            StringBuilder sb = new();
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    sb.Append(grid[i, j]);
                    sb.Append(",");
                }
            }
            return sb.ToString();
        }
    }
}