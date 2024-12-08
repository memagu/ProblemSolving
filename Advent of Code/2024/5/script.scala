//> using scala 3.5

object Solution:
  def part1(file: String): Int =
    import collection.mutable
    import util.matching.Regex

    val splitInput: Array[String] = io.Source.fromFile(file).mkString.replaceAll("\r\n", "\n").replaceAll("\r", "\n").split("\n\n")
    val rulePattern: Regex = """(\d+)\|(\d+)""".r
    val rules: Map[Int, Set[Int]] = splitInput.head.split("\n").map{ case rulePattern(a, b) => (a.toInt, b.toInt) }.groupBy(_._1).mapValues(pair => pair.map(_._2).toSet).toMap
    val updates: Array[Array[Int]] = splitInput.last.split("\n").map(_.split(',').map(_.toInt))

    updates.filter(_.sliding(2).forall{ case Array(a, b) => rules.contains(a) && rules(a).contains(b) }).map(update => update(update.length / 2)).sum

  // Incomplete
  def part2(file: String): Int =
    import collection.mutable
    import util.matching.Regex

    val splitInput: Array[String] = io.Source.fromFile(file).mkString.replaceAll("\r\n", "\n").replaceAll("\r", "\n").split("\n\n")
    val rulePattern: Regex = """(\d+)\|(\d+)""".r
    val rules: Map[Int, Set[Int]] = splitInput.head.split("\n").map{ case rulePattern(a, b) => (a.toInt, b.toInt) }.groupBy(_._1).mapValues(pair => pair.map(_._2).toSet).toMap
    val updates: Array[Array[Int]] = splitInput.last.split("\n").map(_.split(',').map(_.toInt))

    updates.map()
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

