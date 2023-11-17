package com.barneyb.aoc.aoc2020.day05;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class BoardingPassTest {

    @Test
    void exampleFour() {
        var pass = BoardingPass.of("BBFFBBFRLL");
        assertEquals(102, pass.row());
        assertEquals(4, pass.col());
        assertEquals(820, pass.seatId());
    }

}
