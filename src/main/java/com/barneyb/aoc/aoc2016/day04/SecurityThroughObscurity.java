package com.barneyb.aoc.aoc2016.day04;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;
import java.util.List;

public class SecurityThroughObscurity extends SolveEachPart<List<Room>, Long, Long> {

    public static void main(String[] args) {
        new SecurityThroughObscurity().solveAndPrint();
    }

    @Override
    protected List<Room> buildModel(Input input) {
        List<Room> rooms = new ArrayList<>();
        for (String line : input) {
            rooms.add(Room.parse(line));
        }
        return rooms;
    }

    @Override
    protected Long solvePartOne(List<Room> rooms) {
        long sum = 0;
        for (Room r : rooms) {
            if (r.real()) sum += r.sector();
        }
        return sum;
    }

    @Override
    protected Long solvePartTwo(List<Room> rooms) {
        Long sector = null;
        String name = null;
        for (Room r : rooms) {
            if (!r.real()) continue;
            String n = r.name();
            if (n.contains("north") && n.contains("pole")) {
                if (sector != null) {
                    throw new RuntimeException(String.format(
                            "Ambiguous name match. Found '%s' after '%s'",
                            n,
                            name));
                }
                sector = r.sector();
                name = n;
            }
        }
        return sector;
    }

}
