package com.barneyb.aoc.util;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class DigestTest {

    @Test
    void md5hex() {
        assertEquals("000008f82c5b3924a1ecbebf60344e00",
                     Digest.md5hex("abc", 5017308));
    }

}
