import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

class BatteryBank {
    private final String batteryBank;

    public  BatteryBank(String batteryBank) {
        this.batteryBank = batteryBank;
    }

    private String maxJoltage(int batteries, int minIndex) {
        if (batteries == 0) {
            return "";
        }

        int maxIndex = batteryBank.length() - batteries;
        char maxDigit = '0';
        int maxDigitIndex = 0;
        for (int i = minIndex; i <= maxIndex; i++) {
            char digit = batteryBank.charAt(i);
            if (digit > maxDigit) {
                maxDigit = digit; 
                maxDigitIndex = i;
            }
        }

        return maxDigit + maxJoltage(batteries - 1, maxDigitIndex + 1);
    }
    
    public long maxJoltage(int batteries) {
        return Long.parseLong(maxJoltage(batteries, 0));
    }
}

class Solutions {
    static int part1(String data) { 
        int result = 0;

        String[] batteryBanks = data.split("\n");
        for (String batteryBank : batteryBanks) {
            int maxTens = 0;
            int maxOnes = 0;
            for (int i = 0; i < batteryBank.length(); i++) {
                int digit = batteryBank.charAt(i) - '0';

                if (digit > maxTens && i < batteryBank.length() - 1) {
                    maxTens = digit;
                    maxOnes = batteryBank.charAt(i + 1) - '0';
                } else {
                    maxOnes = Math.max(maxOnes, digit);
                }
            }
            result += maxTens * 10 + maxOnes;
        }

        return result;
    }

    static long part2(String data) {
        long result = 0;

        String[] batteryBanks = data.split("\n");
        for (String batteryBank : batteryBanks) {
            result += new BatteryBank(batteryBank).maxJoltage(12);
        }

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

