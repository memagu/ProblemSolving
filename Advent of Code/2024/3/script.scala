//> using scala 3.5

object Solution:
  def part1(file: String): Int =
    raw"mul\((\d{1,3}),(\d{1,3})\)".r.findAllMatchIn(scala.io.Source.fromFile(file).mkString).map(patternMatch => patternMatch.group(1).toInt * patternMatch.group(2).toInt).sum

  def part2(file: String): Int =
    import scala.util.matching.Regex

    val input: String = scala.io.Source.fromFile(file).mkString
    var multiplicationEnabled: Boolean = true
    var result: Int = 0

    val mulPattern: Regex = """^mul\((\d{1,3}),(\d{1,3})\)[\S\s]*$""".r
    val doPattern: Regex = """^do\(\)[\S\s]*$""".r
    val dontPattern: Regex = """^don't\(\)[\S\s]*$""".r

    for i <- input.indices do
      input.substring(i) match
        case mulPattern(a, b) if multiplicationEnabled => result += a.toInt * b.toInt
        case doPattern() => multiplicationEnabled = true
        case dontPattern() => multiplicationEnabled = false
        case _ =>

    result

@main
def main(): Unit =
  import Solution._

  val dataPath: String = "./data.in"
  val examplePath: String = "./example.in"

  println(s"Part 1: ${part1(dataPath)}")
  println(s"Part 1 (example): ${part1(examplePath)}")
  println(s"Part 2: ${part2(dataPath)}")
  println(s"Part 2 (example): ${part2(examplePath)}")

