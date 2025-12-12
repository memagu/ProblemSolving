import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import java.util.ArrayList;
import java.util.List;

class Range {
    public final long start;
    public final long end;

    public Range  (long start, long end) {
        this.start = start;
        this.end = end;
    }

    public boolean contains(long value) {
        return start <= value && value <= end;
    }

    public long size() {
        return end - start + 1;
    }

    public boolean equals(Range other) {
        return start == other.start && end == other.end;
    }

    public boolean canMerge(Range other) {
        return contains(other.start) || 
               contains(other.end)   ||
               other.contains(start) ||
               other.contains(end);
    }

    public Range merge(Range other) {
        return new Range(
            Math.min(start, other.start),
            Math.max(end, other.end)
        );
    }
}

class Database {
    private final List<Range> ranges = new ArrayList<>();

    public  Database(List<Range> ranges) {
        ranges.forEach(this::add);  
    }

    public  Database(String ranges) {
        ranges
            .lines()
            .map(string -> string.split("-"))
            .map(b -> new Range(
                Long.parseLong(b[0]),
                Long.parseLong(b[1])
            ))
            .forEach(this::add);
    }

    public void add(Range range) {
        Range newRange = range;

        while (true) {
            boolean merged = false;

            for (int i = 0; i < ranges.size(); i++) {
                Range existing = ranges.get(i);

                if (existing.canMerge(newRange)) {
                    merged = true; 
                    newRange = existing.merge(newRange);
                    ranges.remove(i);
                    break;
                }
            }   

            if (!merged) {
                ranges.add(newRange);
                return;
            }
        }
    }

    public boolean isFresh(long id) {
        return ranges.stream().anyMatch(range -> range.contains(id));
    }

    public long totalFresh() {
        return ranges.stream().mapToLong(range -> range.size()).sum();
    }
}

class Solutions {
    static long part1(String data) { 
        String[] parts = data.split("\n\n");
        Database db = new Database(parts[0]);

        return parts[1]
        .lines()
        .mapToLong(Long::parseLong)
        .filter(id -> db.isFresh(id))
        .count();

    }

    static long part2(String data) {
        return new Database(data.split("\n\n")[0]).totalFresh();
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

