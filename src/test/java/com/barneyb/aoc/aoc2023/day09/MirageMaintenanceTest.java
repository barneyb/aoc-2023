package com.barneyb.aoc.aoc2023.day09;

import com.barneyb.aoc.NotInCI;
import org.junit.jupiter.api.Test;

class MirageMaintenanceTest {

    @Test
    @NotInCI
    void realWorld() {
        new MirageMaintenance().test(1987402313, 900);
    }

}
