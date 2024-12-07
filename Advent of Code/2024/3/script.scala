//> using scala 3.5

object Solution:
  def part1(file: String): Int =
    raw"mul\((\d{1,3}),(\d{1,3})\)".r.findAllMatchIn(scala.io.Source.fromFile(file).mkString).map(patternMatch => patternMatch.group(1).toInt * patternMatch.group(2).toInt).sum

  // Unfinised
  def part2(file: String): Int =
    raw"mul\((\d{1,3}),(\d{1,3})\)".r.findAllMatchIn(scala.io.Source.fromFile(file).mkString.replaceAll(raw"don't\(\).*?do\(\)", "").reverse.replaceFirst(raw".*\)\(t'nod", "").reverse).map(patternMatch => patternMatch.group(1).toInt * patternMatch.group(2).toInt).sum


@main
def main(): Unit =
  import Solution._

  val dataPath: String = "./data.in"
  val examplePath: String = "./example.in"

  println(s"Part 1: ${part1(dataPath)}")
  println(s"Part 1 (example): ${part1(examplePath)}")
  println(s"Part 2: ${part2(dataPath)}")
  println(s"Part 2 (example): ${part2(examplePath)}")

