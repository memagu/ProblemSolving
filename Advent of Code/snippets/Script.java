import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

class Solutions {
    static int part1(String data) { 
        return 0;
    }

    static int part2(String data) {
        return 0;
     } 
}

class Script {
    public static void main(String[] args) throws IOException {
        String realData = Files.readString(Paths.get("./data.in"));
        String exampleData = Files.readString(Paths.get("./example.in"));

        System.out.printf("Part 1: %d%n", Solutions.part1(realData));
        System.out.printf("Part 1 (example): %d%n", Solutions.part1(exampleData));
        System.out.printf("Part 2: %d%n", Solutions.part2(realData));
        System.out.printf("Part 2 (example): %d%n", Solutions.part2(exampleData));
    }
}

