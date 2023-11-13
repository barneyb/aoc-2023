package com.barneyb.aoc.aoc2016.day02;

import com.barneyb.aoc.geom.Dir;
import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class BathroomSecurity extends SolvePartOne<List<List<Dir>>, String> {

    public static void main(String[] args) {
        new BathroomSecurity().solveAndPrint();
    }

    public static final Map<Point, Character> KEYPAD = Map.of(
            new Point(0, 0), '1',
            new Point(1, 0), '2',
            new Point(2, 0), '3',
            new Point(0, 1), '4',
            new Point(1, 1), '5',
            new Point(2, 1), '6',
            new Point(0, 2), '7',
            new Point(1, 2), '8',
            new Point(2, 2), '9');

    @Override
    protected List<List<Dir>> buildModel(Input input) {
        List<List<Dir>> result = new ArrayList<>();
        for (String line : input) {
            List<Dir> row = new ArrayList<>(line.length());
            for (char c : line.toCharArray()) {
                row.add(Dir.parse(c));
            }
            result.add(row);
        }
        return result;
    }

    @Override
    protected String solvePartOne(List<List<Dir>> lists) {
        StringBuilder sb = new StringBuilder();
        Point curr = new Point(1, 1);
        for (List<Dir> row : lists) {
            for (Dir d : row) {
                Point next = curr.move(d);
                if (KEYPAD.containsKey(next)) {
                    curr = next;
                }
            }
            sb.append(KEYPAD.get(curr));
        }
        return sb.toString();
    }

}
