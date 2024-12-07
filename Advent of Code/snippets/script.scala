//> using scala 3.5

object Solution:
  def part1(file: String): Int =
    scala.io.Source.fromFile(file)
    0

  def part2(file: String): Int =
    scala.io.Source.fromFile(file)
    0

@main
def main(): Unit =
  import Solution._

  val dataPath: String = "./data.in"
  val examplePath: String = "./example.in"

  println(s"Part 1: ${part1(dataPath)}")
  println(s"Part 1 (example): ${part1(examplePath)}")
  println(s"Part 2: ${part2(dataPath)}")
  println(s"Part 2 (example): ${part2(examplePath)}")

