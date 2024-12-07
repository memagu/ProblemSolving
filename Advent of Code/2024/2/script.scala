//> using scala 3.5

object Solution:
  def part1(file: String): Int =
    scala.io.Source.fromFile(file).getLines().map(_.split(" ").map(_.toInt)).count(_.sliding(3).forall {
      case Array(a, b, c) => ((a < b && b < c) || (a > b && b > c)) && Array(a, b, c).sliding(2).forall {
        case Array(x, y) => (1 to 3).contains((x - y).abs)
      }
    })

  // Incomplete
  def part2(file: String): Int =
    scala.io.Source.fromFile(file).getLines().map(_.split(" ").map(_.toInt)).count(_.sliding(3).count {
      case Array(a, b, c) => !(((a < b && b < c) || (a > b && b > c)) && Array(a, b, c).sliding(2).forall {
        case Array(x, y) => (1 to 3).contains((x - y).abs)
      })
    } <= 2)

@main
def main(): Unit =
  import Solution._

  val dataPath: String = "./data.in"
  val examplePath: String = "./example.in"

  println(s"Part 1: ${part1(dataPath)}")
  println(s"Part 1 (example): ${part1(examplePath)}")
  println(s"Part 2: ${part2(dataPath)}")
  println(s"Part 2 (example): ${part2(examplePath)}")

