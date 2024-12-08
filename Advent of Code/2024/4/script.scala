//> using scala 3.5

object Solution:
  def part1(file: String): Int =
    val matrix: Array[String] = scala.io.Source.fromFile(file).getLines.toArray
    val target: String = "XMAS"
    val directions: Array[(Int, Int)] = Array((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

    matrix.indices.flatMap(row => matrix.head.indices.map(column => directions.count((deltaRow, deltaColumn) => target.indices.forall{ i =>
      val newRow: Int = row + deltaRow * i
      val newColumn: Int = column + deltaColumn * i
      matrix.isDefinedAt(newRow) && matrix.head.isDefinedAt(newColumn) && target(i) == matrix(newRow)(newColumn)
    }))).sum

def part2(file: String): Int =
    val matrix: Array[String] = scala.io.Source.fromFile(file).getLines.toArray
    val kernels: Array[Array[Array[Char]]] = Array(
      Array(
        Array('M', '.', 'S'),
        Array('.', 'A', '.'),
        Array('M', '.', 'S')
      ),
      Array(
        Array('M', '.', 'M'),
        Array('.', 'A', '.'),
        Array('S', '.', 'S')
      ),
      Array(
        Array('S', '.', 'M'),
        Array('.', 'A', '.'),
        Array('S', '.', 'M')
      ),
      Array(
        Array('S', '.', 'S'),
        Array('.', 'A', '.'),
        Array('M', '.', 'M')
      )
    )
    (0 until matrix.length - (kernels.head.length - 1)).map(row => (0 until matrix.head.length - (kernels.head.head.length - 1)).count(column => kernels.exists(kernel => kernel.indices.forall(kernelRow => kernel.head.indices.forall(kernelColumn => kernel(kernelRow)(kernelColumn) == '.' || kernel(kernelRow)(kernelColumn) == matrix(row + kernelRow)(column + kernelColumn)))))).sum

@main
def main(): Unit =
  import Solution._

  val dataPath: String = "./data.in"
  val examplePath: String = "./example.in"

  println(s"Part 1: ${part1(dataPath)}")
  println(s"Part 1 (example): ${part1(examplePath)}")
  println(s"Part 2: ${part2(dataPath)}")
  println(s"Part 2 (example): ${part2(examplePath)}")

