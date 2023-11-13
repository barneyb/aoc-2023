package com.barneyb.aoc.aoc2016.day02;

import com.barneyb.aoc.geom.Dir;
import com.barneyb.aoc.geom.Point;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BathroomSecurity extends SolveEachPart<List<List<Dir>>, String, String> {

    public static void main(String[] args) {
        new BathroomSecurity().solveAndPrint();
    }

    private static final Map<Point, Character> KEYPAD_ONE = Map.of(
            new Point(0, 0), '1',
            new Point(1, 0), '2',
            new Point(2, 0), '3',
            new Point(0, 1), '4',
            new Point(1, 1), '5',
            new Point(2, 1), '6',
            new Point(0, 2), '7',
            new Point(1, 2), '8',
            new Point(2, 2), '9');

    private static final Map<Point, Character> KEYPAD_TWO;

    static {
        Map<Point, Character> map = new HashMap<>();
        map.put(new Point(2, 0), '1');
        map.put(new Point(1, 1), '2');
        map.put(new Point(2, 1), '3');
        map.put(new Point(3, 1), '4');
        map.put(new Point(0, 2), '5');
        map.put(new Point(1, 2), '6');
        map.put(new Point(2, 2), '7');
        map.put(new Point(3, 2), '8');
        map.put(new Point(4, 2), '9');
        map.put(new Point(1, 3), 'A');
        map.put(new Point(2, 3), 'B');
        map.put(new Point(3, 3), 'C');
        map.put(new Point(2, 4), 'D');
        KEYPAD_TWO = Collections.unmodifiableMap(map);
    }

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
        return solve(lists, KEYPAD_ONE);
    }

    private String solve(List<List<Dir>> lists,
                         Map<Point, Character> keypad) {
        StringBuilder sb = new StringBuilder();
        Point curr = start(keypad);
        for (List<Dir> row : lists) {
            for (Dir d : row) {
                Point next = curr.move(d);
                if (keypad.containsKey(next)) {
                    curr = next;
                }
            }
            sb.append(keypad.get(curr));
        }
        return sb.toString();
    }

    private Point start(Map<Point, Character> keypad) {
        Point curr = null;
        for (Map.Entry<Point, Character> e : keypad.entrySet()) {
            if ('5' == e.getValue()) {
                curr = e.getKey();
            }
        }
        if (curr == null) {
            throw new RuntimeException("Failed to find '5' key");
        }
        return curr;
    }

    @Override
    protected String solvePartTwo(List<List<Dir>> lists) {
        return solve(lists, KEYPAD_TWO);
    }

}
