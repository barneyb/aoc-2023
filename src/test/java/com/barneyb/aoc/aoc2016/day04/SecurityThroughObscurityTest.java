package com.barneyb.aoc.aoc2016.day04;

import com.barneyb.aoc.util.Input;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SecurityThroughObscurityTest {

    @Test
    void exampleOne() {
        var solver = new SecurityThroughObscurity();
        var rooms = solver.buildModel(Input.of(
                """
                        aaaaa-bbb-z-y-x-123[abxyz]
                        a-b-c-d-e-f-g-h-987[abcde]
                        not-a-real-room-404[oarel]
                        totally-real-room-200[decoy]"""));
        assertEquals(1514, solver.solvePartOne(rooms));
    }

    @Test
    void realWorld() {
        new SecurityThroughObscurity().test(361724);
    }

}
