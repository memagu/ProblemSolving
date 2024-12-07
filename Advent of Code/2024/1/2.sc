//> using scala 3.5

val Array(left, right) = scala.io.Source.fromFile("./input").getLines.map(_.split("   ", 2).map(_.toInt)).toArray.transpose 

println(left.distinct.map(x => x * right.count(_ == x)).sum)

