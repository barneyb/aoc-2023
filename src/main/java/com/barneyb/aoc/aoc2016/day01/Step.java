package com.barneyb.aoc.aoc2016.day01;

public record Step(Turn turn, Long distance) {

    public static Step parse(String s) {
        return new Step(Turn.parse(s.charAt(0)),
                        Long.parseLong(s.substring(1)));
    }

}
