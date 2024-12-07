//> using scala 3.5

object Solution:
  def part1(file: String): Int =
    scala.io.Source.fromFile(file).getLines.map(_.split("   ").map(_.toInt)).toArray.transpose.map(_.sorted).transpose.map(a => math.abs(a(0) - a(1))).sum

  def part2(file: String): Int =
    val Array(left, right) = scala.io.Source.fromFile(file).getLines.map(_.split("   ", 2).map(_.toInt)).toArray.transpose

    left.distinct.map(x => x * right.count(_ == x)).sum

@main
def main(): Unit =
  import Solution._

  val dataPath: String = "./data.in"
  val examplePath: String = "./example.in"

  println(s"Part 1: ${part1(dataPath)}")
  println(s"Part 1 (example): ${part1(examplePath)}")
  println(s"Part 2: ${part2(dataPath)}")
  println(s"Part 2 (example): ${part2(examplePath)}")
