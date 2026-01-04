package com.barneyb.aoc.util;

import java.util.Objects;

public record Answers<One, Two>(One partOne, Two partTwo) {

    public Answers<String, String> stringify() {
        return new Answers<>(partOne == null ? null : Objects.toString(partOne),
                             partTwo == null ? null : Objects.toString(partTwo));
    }

}
