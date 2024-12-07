

final class `2$_` {
def args = `2_sc`.args$
def scriptPath = """2.sc"""
/*<script>*/
//> using scala 3.5

val Array(left, right) = scala.io.Source.fromFile("./input").getLines.map(_.split("   ", 2).map(_.toInt)).toArray.transpose 

println(left.distinct.map(x => x * right.count(_ == x)).sum)


/*</script>*/ /*<generated>*//*</generated>*/
}

object `2_sc` {
  private var args$opt0 = Option.empty[Array[String]]
  def args$set(args: Array[String]): Unit = {
    args$opt0 = Some(args)
  }
  def args$opt: Option[Array[String]] = args$opt0
  def args$: Array[String] = args$opt.getOrElse {
    sys.error("No arguments passed to this script")
  }

  lazy val script = new `2$_`

  def main(args: Array[String]): Unit = {
    args$set(args)
    val _ = script.hashCode() // hashCode to clear scalac warning about pure expression in statement position
  }
}

export `2_sc`.script as `2`

