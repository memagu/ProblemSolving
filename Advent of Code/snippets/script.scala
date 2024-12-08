//> using scala 3.5

object Solution:
  def part1(input: BufferedSource): Int =
    0

  def part2(input: BufferedSource): Int =
    0

@main
def main(): Unit =
  import Solution._

  val dataInput: String = io.Source.fromFile("./data.in")
  val exampleInput: String = io.Source.fromFile("./example.in")

  println(s"Part 1: ${part1(dataInput)}")
  println(s"Part 1 (example): ${part1(exampleInput)}")
  println(s"Part 2: ${part2(dataInput)}")
  println(s"Part 2 (example): ${part2(exampleInput)}")

