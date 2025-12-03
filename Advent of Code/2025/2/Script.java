import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

class Solutions {
    static long part1(String data) { 
        long result = 0;

        String[] idRanges = data.split(",");
        for (String idRange : idRanges) {
            String[] idRangeEdges = idRange.split("-");
            long idRangeStart = Long.parseLong(idRangeEdges[0]);
            long idRangeEnd = Long.parseLong(idRangeEdges[1]); 

            for (long id = idRangeStart; id <= idRangeEnd; id++) {
                String idString = String.valueOf(id);
                if (idString.length() % 2 == 1) {
                    id = (long) Math.pow(10.0, (double) idString.length()) - 1;
                    continue;
                }

                int midIndex = idString.length() / 2;
                if (idString.substring(0, midIndex).equals(idString.substring(midIndex))) {
                    result += id;
                }
            }
        }

        return result;
    }

    static long part2(String data) {
        long result = 0;

        String[] idRanges = data.split(",");
        for (String idRange : idRanges) {
            String[] idRangeEdges = idRange.split("-");
            long idRangeStart = Long.parseLong(idRangeEdges[0]);
            long idRangeEnd = Long.parseLong(idRangeEdges[1]); 

            for (long id = idRangeStart; id <= idRangeEnd; id++) {
                String idString = String.valueOf(id);

                boolean isValidId = true;
                for (int atomLength = 1; isValidId && atomLength <= idString.length() / 2; atomLength++) {
                    String atom = idString.substring(0, atomLength);

                    boolean repeats = idString.length() % atomLength == 0;
                    for (int chunkIndex = atomLength; repeats && chunkIndex + atomLength <= idString.length(); chunkIndex += atomLength) {
                        if (!idString.substring(chunkIndex, chunkIndex + atomLength).equals(atom)) {
                            repeats = false;
                            break;
                        }
                    }

                    if (repeats) {
                        result += id;
                        isValidId = false;
                    }
                }
            }
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

