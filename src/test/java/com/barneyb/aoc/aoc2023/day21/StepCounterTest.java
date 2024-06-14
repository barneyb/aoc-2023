package com.barneyb.aoc.aoc2023.day21;

import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class StepCounterTest {

    private static final String EXAMPLE_ONE =
            """
            ...........
            .....###.#.
            .###.##..#.
            ..#.#...#..
            ....#.#....
            .##..S####.
            .##..#...#.
            .......##..
            .##.#.####.
            .##..##.##.
            ...........
            """;

    private static final String CAN_BE_EXPANDED =
            """
            ...........
            ......##.#.
            .###..#..#.
            ..#.#...#..
            .#..#.#.##.
            .....S.....
            .##......#.
            .......##..
            .##.#.####.
            .##...#.##.
            ...........
            """;

    private String expand(int n, String base) {
        n = n * 2 + 1;
        var lines = base.split("\\n");
        int mid = lines.length / 2;
        lines[mid] = lines[mid].replace('S', '.');
        for (int i = 0; i < lines.length; i++)
            lines[i] = lines[i].repeat(n) + '\n';
        var rows = new String[n];
        Arrays.fill(rows, String.join("", lines));
        var expanded = String.join("", rows);
        int idx = expanded.length() / 2 - 1;
        return expanded.substring(0, idx) + 'S' + expanded.substring(idx + 1);
    }

    @Test
    void parsing() {
        StepCounter solver = new StepCounter();
        Model model = solver.buildModel(Input.of(EXAMPLE_ONE));
        assertEquals(List.of(Point.of(5, 4),
                             Point.of(4, 5)),
                     model.graph().adjacent(model.start()));
        assertEquals(List.of(Point.of(3, 6),
                             Point.of(2, 7),
                             Point.of(4, 7),
                             Point.of(3, 8)),
                     model.graph().adjacent(Point.of(3, 7)));
        assertEquals(List.of(),
                     model.graph().adjacent(Point.of(7, 5)));
        assertEquals(List.of(),
                     model.graph().adjacent(Point.of(8, 8)));
    }

    @Test
    void examplesOne() {
        StepCounter solver = new StepCounter();
        Model model = solver.buildModel(Input.of(EXAMPLE_ONE));
        assertEquals(2, solver.solvePartOne(model, 1));
        assertEquals(4, solver.solvePartOne(model, 2));
        assertEquals(6, solver.solvePartOne(model, 3));
        assertEquals(16, solver.solvePartOne(model, 6));
    }

    @Test
    void three() {
        var garden = """
                     ...
                     .S.
                     ...
                     """;
        for (int i = 0; i < 50; i++) {
            draw(i, garden, true);
        }
    }

    @Test
    void five() {
        var garden = """
                     .....
                     .....
                     ..S..
                     .....
                     .....
                     """;
        for (int i = 0; i < 50; i++) {
            draw(i, garden, true);
        }
    }

    @Test
    void seven() {
        var garden = """
                     .......
                     .......
                     .......
                     ...S...
                     .......
                     .......
                     .......
                     """;
        for (int i = 0; i < 50; i++) {
            draw(i, garden, true);
        }
    }

    @Test
    void canBeExpanded() {
        StepCounter solver = new StepCounter();
        Model model = solver.buildModel(Input.of(CAN_BE_EXPANDED));
        assertEquals(1, solver.solvePartTwo(model, 0));
        assertEquals(4, solver.solvePartTwo(model, 1));
        assertEquals(7, solver.solvePartTwo(model, 2));
        assertEquals(15, solver.solvePartTwo(model, 3));
        assertEquals(24, solver.solvePartTwo(model, 5));
        assertEquals(33, solver.solvePartTwo(model, 6));
        assertEquals(46, solver.solvePartTwo(model, 7));
        assertEquals(60, solver.solvePartTwo(model, 8));
        assertEquals(76, solver.solvePartTwo(model, 9));
        assertEquals(87, solver.solvePartTwo(model, 10));
        assertEquals(100, solver.solvePartTwo(model, 11));
        assertEquals(122, solver.solvePartTwo(model, 12));
        assertEquals(137, solver.solvePartTwo(model, 13));
        assertEquals(169, solver.solvePartTwo(model, 14));
        assertEquals(186, solver.solvePartTwo(model, 15));
        assertEquals(207, solver.solvePartTwo(model, 16));
        assertEquals(227, solver.solvePartTwo(model, 17));
        assertEquals(258, solver.solvePartTwo(model, 18));
        assertEquals(289, solver.solvePartTwo(model, 19));
        assertEquals(325, solver.solvePartTwo(model, 20));
        assertEquals(350, solver.solvePartTwo(model, 21));
        assertEquals(375, solver.solvePartTwo(model, 22));
        assertEquals(416, solver.solvePartTwo(model, 23));
        assertEquals(443, solver.solvePartTwo(model, 24));
        assertEquals(499, solver.solvePartTwo(model, 25));
        assertEquals(694, solver.solvePartTwo(model, 30));
        assertEquals(925, solver.solvePartTwo(model, 35));
        assertEquals(1210, solver.solvePartTwo(model, 40));
        assertEquals(1532, solver.solvePartTwo(model, 45));
        assertEquals(1865, solver.solvePartTwo(model, 50));
    }

    @SuppressWarnings("unused")
    private void draw(int steps) {
        draw(steps, CAN_BE_EXPANDED, false);
    }

    private void draw(int steps, String base, boolean oneQuadrant) {
        StepCounter solver = new StepCounter();
        Model m = solver.buildModel(Input.of(base));
        int dim = m.dim();
        int exFactor = (int) Math.ceil((double) (steps - m.half()) / dim);
        int start = oneQuadrant ? dim * exFactor : 0;
        Model model = solver.buildModel(Input.of(expand(exFactor, base)));
        var ps = solver.buildTrace(model).get(steps);
        var sb = new StringBuilder();
        for (int y = start; y <= model.max(); y++) {
            if (y > 0 && y % dim == 0) sb.append('\n');
            for (int x = start; x <= model.max(); x++) {
                if (x > 0 && x % dim == 0) sb.append("  ");
                Point p = Point.of(x, y);
                sb.append(ps.contains(p) ? 'O' : model.graph().vertices().contains(p) ? '.' : '#');
            }
            sb.append('\n');
        }
        int width = sb.indexOf("\n");
        bar("Step " + steps, width);
        System.out.print(sb);
        Long one = solver.solvePartOne(model, steps);
        Long two = solver.solvePartTwo(m, steps);
        bar(one + " :: " + two, width);
        assertEquals(one, two);
        System.out.println();
    }

    private static void bar(String lbl, int width) {
        String prefix = "-- " + lbl + " --";
        System.out.println(prefix + "-".repeat(Math.max(0, width - prefix.length())));
    }

    @Test
    void realInput() {
        StepCounter solver = new StepCounter();
        Model m = solver.buildModel(Input.of(StepCounter.class));
        assertEquals(3_788L, solver.solvePartOne(m));
        assertEquals(631_357_596_621_921L, solver.solvePartTwo(m));
    }

    @Test
    void verifyExpanded() {
        assertEquals("""
                     .................................
                     .....###.#......###.#......###.#.
                     .###.##..#..###.##..#..###.##..#.
                     ..#.#...#....#.#...#....#.#...#..
                     ....#.#........#.#........#.#....
                     .##...####..##...####..##...####.
                     .##..#...#..##..#...#..##..#...#.
                     .......##.........##.........##..
                     .##.#.####..##.#.####..##.#.####.
                     .##..##.##..##..##.##..##..##.##.
                     .................................
                     .................................
                     .....###.#......###.#......###.#.
                     .###.##..#..###.##..#..###.##..#.
                     ..#.#...#....#.#...#....#.#...#..
                     ....#.#........#.#........#.#....
                     .##...####..##..S####..##...####.
                     .##..#...#..##..#...#..##..#...#.
                     .......##.........##.........##..
                     .##.#.####..##.#.####..##.#.####.
                     .##..##.##..##..##.##..##..##.##.
                     .................................
                     .................................
                     .....###.#......###.#......###.#.
                     .###.##..#..###.##..#..###.##..#.
                     ..#.#...#....#.#...#....#.#...#..
                     ....#.#........#.#........#.#....
                     .##...####..##...####..##...####.
                     .##..#...#..##..#...#..##..#...#.
                     .......##.........##.........##..
                     .##.#.####..##.#.####..##.#.####.
                     .##..##.##..##..##.##..##..##.##.
                     .................................
                     """, expand(1,
                                 EXAMPLE_ONE));
        assertEquals("""
                     .................................
                     ......##.#.......##.#.......##.#.
                     .###..#..#..###..#..#..###..#..#.
                     ..#.#...#....#.#...#....#.#...#..
                     .#..#.#.##..#..#.#.##..#..#.#.##.
                     .................................
                     .##......#..##......#..##......#.
                     .......##.........##.........##..
                     .##.#.####..##.#.####..##.#.####.
                     .##...#.##..##...#.##..##...#.##.
                     .................................
                     .................................
                     ......##.#.......##.#.......##.#.
                     .###..#..#..###..#..#..###..#..#.
                     ..#.#...#....#.#...#....#.#...#..
                     .#..#.#.##..#..#.#.##..#..#.#.##.
                     ................S................
                     .##......#..##......#..##......#.
                     .......##.........##.........##..
                     .##.#.####..##.#.####..##.#.####.
                     .##...#.##..##...#.##..##...#.##.
                     .................................
                     .................................
                     ......##.#.......##.#.......##.#.
                     .###..#..#..###..#..#..###..#..#.
                     ..#.#...#....#.#...#....#.#...#..
                     .#..#.#.##..#..#.#.##..#..#.#.##.
                     .................................
                     .##......#..##......#..##......#.
                     .......##.........##.........##..
                     .##.#.####..##.#.####..##.#.####.
                     .##...#.##..##...#.##..##...#.##.
                     .................................
                     """, expand(1,
                                 CAN_BE_EXPANDED));
        StepCounter solver = new StepCounter();
        Model model = solver.buildModel(Input.of(expand(5,
                                                        CAN_BE_EXPANDED)));
        var trace = solver.buildTrace(model);
        assertEquals(1, trace.get(0).size());
        assertEquals(4, trace.get(1).size());
        assertEquals(7, trace.get(2).size());
        assertEquals(15, trace.get(3).size());
        assertEquals(33, trace.get(6).size());
        assertEquals(46, trace.get(7).size());
        assertEquals(60, trace.get(8).size());
        assertEquals(76, trace.get(9).size());
        assertEquals(87, trace.get(10).size());
        assertEquals(100, trace.get(11).size());
        assertEquals(122, trace.get(12).size());
        assertEquals(137, trace.get(13).size());
        assertEquals(169, trace.get(14).size());
        assertEquals(186, trace.get(15).size());
        assertEquals(207, trace.get(16).size());
        assertEquals(227, trace.get(17).size());
        assertEquals(258, trace.get(18).size());
        assertEquals(289, trace.get(19).size());
        assertEquals(325, trace.get(20).size());
        assertEquals(350, trace.get(21).size());
        assertEquals(375, trace.get(22).size());
        assertEquals(416, trace.get(23).size());
        assertEquals(443, trace.get(24).size());
        assertEquals(499, trace.get(25).size());
        assertEquals(694, trace.get(30).size());
        assertEquals(925, trace.get(35).size());
        assertEquals(1210, trace.get(40).size());
        assertEquals(1532, trace.get(45).size());
        assertEquals(1865, trace.get(50).size());
    }

    @ParameterizedTest
    @CsvSource(textBlock = """
                           0,   0
                           1,   1
                           2,   3
                           3,   6
                           4,   10
                           5,   15
                           6,   21
                           7,   28
                           """)
    void triangleNumbers(long n, long tri) {
        assertEquals(tri, StepCounter.triangle(n));
    }

    @ParameterizedTest
    @CsvSource(textBlock = """
                           0,   0
                           1,   1
                           2,   2
                           3,   4
                           4,   6
                           5,   9
                           6,   12
                           7,   16
                           """)
    void halftoneTriangleNumbers(long n, long htTri) {
        assertEquals(htTri, StepCounter.halftone_triangle(n));
    }

}
