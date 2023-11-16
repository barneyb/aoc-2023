package com.barneyb.aoc.aoc2019.day02;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class IntcodeTest {

    @Test
    void exampleOne() {
        var vm = new Intcode(new int[]{ 1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50 });
        vm.run();
        assertEquals(3500, vm.getPosition(0));
        assertEquals(70, vm.getPosition(3));
    }

    @Test
    void exampleTwo() {
        var vm = new Intcode(new int[]{ 1, 0, 0, 0, 99 });
        vm.run();
        assertEquals(2, vm.getPosition(0));
    }

    @Test
    void exampleThree() {
        var vm = new Intcode(new int[]{ 2, 3, 0, 3, 99 });
        vm.run();
        assertEquals(6, vm.getPosition(3));
    }

    @Test
    void exampleFour() {
        var vm = new Intcode(new int[]{ 2, 4, 4, 5, 99, 0 });
        vm.run();
        assertEquals(9801, vm.getPosition(5));
    }

    @Test
    void exampleFive() {
        var vm = new Intcode(new int[]{ 1, 1, 1, 4, 99, 5, 6, 0, 99 });
        vm.run();
        assertEquals(30, vm.getPosition(0));
        assertEquals(2, vm.getPosition(4));
    }

}
