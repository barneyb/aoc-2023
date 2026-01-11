package com.barneyb.aoc.aoc2019.day02;

import com.barneyb.aoc.NotInCI;
import org.junit.jupiter.api.Test;

class TwelveZeroTwoProgramAlarmTest {

    @Test
    @NotInCI
    void realWorld() {
        new TwelveZeroTwoProgramAlarm().test(4090689, 7733);
    }

}
