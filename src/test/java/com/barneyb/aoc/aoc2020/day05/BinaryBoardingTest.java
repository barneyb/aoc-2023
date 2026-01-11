package com.barneyb.aoc.aoc2020.day05;

import com.barneyb.aoc.NotInCI;
import org.junit.jupiter.api.Test;

class BinaryBoardingTest {

    @Test
    @NotInCI
    void realWorld() {
        new BinaryBoarding().test(842, 617);
    }

}
