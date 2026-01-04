package com.barneyb.aoc.util;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;

@Slf4j
class AocAllTest {

    @Test
    void support() {
        AocAll.main(new String[]{ "support" });
    }

    @Test
    void solve() {
        System.out.println(new AocAll()
                                   .solve(new AocAll.Day(2015, 1),
                                          "()())"));
    }

}
