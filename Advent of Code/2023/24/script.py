from typing import Sequence

import sympy


def part1():
    with open("data.in", 'r') as f:
        hailstones = []
        for line in f.read().splitlines():
            pos, velocity = line.split(" @ ")
            pos = tuple(map(int, pos.split(", ")))
            velocity = tuple(map(int, velocity.split(", ")))

            hailstones.append((pos, velocity))

    result = 0
    for i, ((x1, y1, _), (dx1, dy1, _)) in enumerate(hailstones):
        for (x2, y2, _), (dx2, dy2, _) in hailstones[i + 1:]:
            """
            x1 + dx1 * u = x2 + dx2 * v
            y1 + dy1 * u = y2 + dy2 * v

            u = (x2 + dx2 * v - x1) / dx1
            u = (y2 + dy2 * v - y1) / dy1

            (x2 + dx2 * v - x1) / dx1 = (y2 + dy2 * v - y1) / dy1
            
            (x2 + dx2 * v - x1) * dy1 = (y2 + dy2 * v - y1) * dx1
            
            x2 * dy1 + dx2 * dy1 * v - x1*dy1 = y2 * dx1 + dy2 * dx1 * v - y1 * dx1
            
            dx2 * dy1 * v - dy2 * dx1 * v = y2 * dx1 - y1 * dx1 - x2 * dy1 + x1*dy1
            
            (dx2 * dy1 - dy2 * dx1) * v = y2 * dx1 - y1 * dx1 - x2 * dy1 + x1*dy1
            
            (dx2 * dy1 - dy2 * dx1) * v = y2 * dx1 - y1 * dx1 - x2 * dy1 + x1*dy1
            
            v = (y2 * dx1 - y1 * dx1 - x2 * dy1 + x1*dy1) / (dx2 * dy1 - dy2 * dx1)
            """

            v_num, v_den = (y2 * dx1 - y1 * dx1 - x2 * dy1 + x1 * dy1), (dx2 * dy1 - dy2 * dx1)
            if not v_den:
                continue
            v = v_num / v_den

            u_num, u_den = (x2 + dx2 * v - x1), dx1
            if not u_den:
                continue
            u = u_num / u_den

            if u < 0 or v < 0:
                continue

            x, y = x1 + dx1 * u, y1 + dy1 * u

            result += 2e14 <= x <= 4e14 and 2e14 <= y <= 4e14

    return result


def part2():
    with open("data.in", 'r') as f:
        hailstones = []
        for line in f.read().splitlines():
            pos, velocity = line.split(" @ ")
            pos = tuple(map(int, pos.split(", ")))
            velocity = tuple(map(int, velocity.split(", ")))

            hailstones.append((pos, velocity))

    """
    xr + vxr * ti = xi + vxi * ti

    vxr * ti - vxi * ti = xi - xr

    ti * (vxr - vxi) = xi - xr

    ti = (xi - xr) / (vxr - vxi)

    The same for y and z:
    ti = (xi - xr) / (vxr - vxi) = (yi - yr) / (vyr - vyi) = (zi - zr) / (vzr - vzi)

    Split the equality into two equations: x=y and y=x.
    (xi - xr) / (vxr - vxi) = (yi - yr) / (vyr - vyi)
    (yi - yr) / (vyr - vyi) = (zi - zr) / (vzr - vzi)

    (xi - xr) * (vyr - vyi) = (yi - yr) * (vxr - vxi)
    (yi - yr) * (vzr - vzi) = (zi - zr) * (vyr - vyi)

    Rewrite in homogeneous form.
    (xi - xr) * (vyr - vyi) - (yi - yr) * (vxr - vxi) = 0
    (yi - yr) * (vzr - vzi) - (zi - zr) * (vyr - vyi) = 0
    
    Create a system of equations containing one pair of the derived equations for each i.
    {
        (xi - xr) * (vyr - vyi) - (yi - yr) * (vxr - vxi) = 0
        (yi - yr) * (vzr - vzi) - (zi - zr) * (vyr - vyi) = 0
        ...
    }
    """

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr", integer=True)

    equations = []
    for (xi, yi, zi), (vxi, vyi, vzi) in hailstones:
        equations.extend(
            (
                (xi - xr) * (vyr - vyi) - (yi - yr) * (vxr - vxi),
                (yi - yr) * (vzr - vzi) - (zi - zr) * (vyr - vyi)
            )
        )

    solutions = sympy.solve(equations, xr, yr, zr, vxr, vyr, vzr)

    x, y, z, _, _, _ = solutions[0]

    return x + y + z


if __name__ == "__main__":
    print(part1())
    print(part2())
