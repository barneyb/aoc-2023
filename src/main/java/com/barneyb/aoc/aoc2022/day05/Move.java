package com.barneyb.aoc.aoc2022.day05;

public record Move(int count, int from, int to) {

    public static Move parse(String str) {
        var parts = str.split(" ");
        return new Move(Integer.parseInt(parts[1]),
                        Integer.parseInt(parts[3]),
                        Integer.parseInt(parts[5]));
    }

}
