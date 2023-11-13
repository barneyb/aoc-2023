package com.barneyb.aoc.aoc2016.day01;

public record State(Point position, Heading heading) {

    public static final State ORIGIN = new State(Point.ORIGIN,
                                                 Heading.NORTH);

    public State turn(Turn turn) {
        return new State(position,
                         heading.turn(turn));
    }

    public State move(Long distance) {
        return new State(position.move(heading,
                                       distance),
                         heading);
    }

    public State move(Step s) {
        return turn(s.turn())
                .move(s.distance());
    }

    public long manhattanDistance() {
        return position.manhattanDistance();
    }

}
