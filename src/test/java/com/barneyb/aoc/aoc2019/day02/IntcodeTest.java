package com.barneyb.aoc.aoc2019.day02;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class IntcodeTest {

    @Test
    void exampleOne() {
        var vm = new Intcode(new int[]{ 1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50 });
        vm.run();
        assertEquals(3500, vm.read(0));
        assertEquals(70, vm.read(3));
    }

    @Test
    void exampleTwo() {
        var vm = new Intcode(new int[]{ 1, 0, 0, 0, 99 });
        vm.run();
        assertEquals(2, vm.read(0));
    }

    @Test
    void exampleThree() {
        var vm = new Intcode(new int[]{ 2, 3, 0, 3, 99 });
        vm.run();
        assertEquals(6, vm.read(3));
    }

    @Test
    void exampleFour() {
        var vm = new Intcode(new int[]{ 2, 4, 4, 5, 99, 0 });
        vm.run();
        assertEquals(9801, vm.read(5));
    }

    @Test
    void exampleFive() {
        var vm = new Intcode(new int[]{ 1, 1, 1, 4, 99, 5, 6, 0, 99 });
        vm.run();
        assertEquals(30, vm.read(0));
        assertEquals(2, vm.read(4));
    }

    @Test
    void dayFiveExampleOne() {
        var vm = new Intcode(new int[]{ 1002, 4, 3, 4, 33 });
        vm.run();
        assertEquals(99, vm.read(4));
    }

}
