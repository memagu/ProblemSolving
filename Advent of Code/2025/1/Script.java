import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

class Safe {
    private int dial = 50;

    public void rotateDial(int steps) {
        dial = (dial + steps) % 100;
    }
    
    public boolean isAtZero() {
        return dial == 0;
    }
}

class Solutions {
    static int part1(String data) { 
        Safe safe = new Safe();

        int code = 0;

        for (String rotation : data.split("\n")) {
            int direction = (rotation.charAt(0) == 'R') ? 1 : -1;
            int steps = Integer.parseInt(rotation.substring(1));

            safe.rotateDial(steps * direction);

            if (safe.isAtZero()) {
                code++;
            }
        } 

        return code;
    }

    static int part2(String data) {
        Safe safe = new Safe();

        int code = 0;

        for (String rotation : data.split("\n")) {
            int direction = (rotation.charAt(0) == 'R') ? 1 : -1;
            int steps = Integer.parseInt(rotation.substring(1));

            for (int i = 0; i < steps; i++) {
                safe.rotateDial(direction);

                if (safe.isAtZero()) {
                    code++;
                }
            }
        } 

        return code;
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

