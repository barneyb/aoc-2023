package com.barneyb.aoc.aoc2018.day05;

public record Unit(char type, boolean polarity) {

    public static Unit of(char c) {
        return Character.isUpperCase(c)
                ? new Unit(Character.toLowerCase(c), true)
                : new Unit(c, false);
    }

    public boolean isReactive(Unit other) {
        return type == other.type
                && polarity != other.polarity;
    }

    @Override
    public String toString() {
        String s = Character.toString(type);
        if (polarity) s = s.toUpperCase();
        return s;
    }

}
