import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import java.util.function.BiConsumer;

class ForkliftArea {
    final boolean[][] data;
    final int cols, rows;

    public  ForkliftArea(String rawData) {
        String[] lines = rawData.split("\n"); 

        rows = lines.length;
        cols = lines[0].length();

        data = new boolean[rows][cols];

        for (int row = 0; row < rows; row++) {
            String line = lines[row];
            for (int col = 0; col < cols; col++) {
                data[row][col] = line.charAt(col) == '@';
            }
        }
    }

    boolean inBounds(int row, int col) {
        return 0 <= row && row < rows && 0 <= col && col < cols;
    }

    void forEachIndex(BiConsumer<Integer, Integer> func) {
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                func.accept(row, col);
            }
        }
    }

    boolean isPaperRoll(int row, int col) {
        return data[row][col];
    }

    int adjacentPaperRolls(int row, int col) {
        int count = 0;

        for (int deltaRow = -1; deltaRow <= 1; deltaRow++) {
            int i = row + deltaRow;
            for (int deltaCol = -1; deltaCol <= 1; deltaCol++) {
                int j = col + deltaCol;

                if ((deltaRow != 0 || deltaCol != 0) && inBounds(i, j) && isPaperRoll(i, j)) {
                    count++;
                }
            }
        }

        return count;
    }

    void removePaperRoll(int row, int col) {
        if (inBounds(row, col)) {
            data[row][col] = false;
        }
    }
}

class Solutions {
    static int part1(String data) { 
        final int[] result = {0};

        ForkliftArea forkliftArea = new ForkliftArea(data);
        forkliftArea.forEachIndex((row, col) -> {
            if (forkliftArea.isPaperRoll(row, col) && forkliftArea.adjacentPaperRolls(row, col) < 4) {
                result[0]++;
            }
        });
        
        return result[0];
    }

    static int part2(String data) {
        int result = 0;

        ForkliftArea forkliftArea = new ForkliftArea(data);
        final int[] picked = {0};
        do {
            picked[0] = 0;
            forkliftArea.forEachIndex((row, col) -> {
                if (forkliftArea.isPaperRoll(row, col) && forkliftArea.adjacentPaperRolls(row, col) < 4) {
                    picked[0]++;
                    forkliftArea.removePaperRoll(row, col);
                }
            });

            result += picked[0];
        } while (picked[0] != 0);
        
        return result;
     } 
}

class Script {
    public static void main(String[] args) throws IOException {
        String realData = Files.readString(Paths.get("./data.in")).strip();
        String exampleData = Files.readString(Paths.get("./example.in")).strip();

        System.out.printf("Part 1: %d%n", Solutions.part1(realData));
        System.out.printf("Part 1 (example): %d%n", Solutions.part1(exampleData));
        System.out.printf("Part 2: %d%n", Solutions.part2(realData));
        System.out.printf("Part 2 (example): %d%n", Solutions.part2(exampleData));
    }
}

