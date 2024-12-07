//> using scala 3.5

println(scala.io.Source.fromFile("./input").getLines.map(_.split("   ").map(_.toInt)).toArray.transpose.map(_.sorted).transpose.map(a => math.abs(a(0) - a(1))).sum)

