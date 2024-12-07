

final class `1$_` {
def args = `1_sc`.args$
def scriptPath = """/home/memagu/Dev/ProblemSolving/Advent of Code/2024/1/1.sc"""
/*<script>*/
//> using scala 3.5

println(scala.io.Source.fromFile("./input").getLines.map(_.split("   ").map(_.toInt)).toArray.transpose.map(_.sorted).transpose.map(a => math.abs(a(0) - a(1))).sum)


/*</script>*/ /*<generated>*//*</generated>*/
}

object `1_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `1$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    val _ = script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `1_sc`.script as `1`

