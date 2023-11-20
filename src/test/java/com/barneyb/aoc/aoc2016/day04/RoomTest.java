package com.barneyb.aoc.aoc2016.day04;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class RoomTest {

    @Test
    void parse() {
        var r = Room.parse("aaaaa-bbb-z-y-x-123[abxyz]");
        assertEquals("aaaaa-bbb-z-y-x", r.encName());
        assertEquals(123, r.sector());
        assertEquals("abxyz", r.chksum());
    }

    @Test
    void isReal() {
        assertTrue(Room.parse("aaaaa-bbb-z-y-x-123[abxyz]").real());
        assertTrue(Room.parse("a-b-c-d-e-f-g-h-987[abcde]").real());
        assertTrue(Room.parse("not-a-real-room-404[oarel]").real());
        assertFalse(Room.parse("totally-real-room-200[decoy]").real());
    }

}
