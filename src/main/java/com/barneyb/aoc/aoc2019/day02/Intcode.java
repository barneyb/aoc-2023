package com.barneyb.aoc.aoc2019.day02;

import java.util.Arrays;

public class Intcode {

    private final int[] memory;
    private int ip;

    public Intcode(int[] program) {
        memory = Arrays.copyOf(program, program.length);
    }

    public int getPosition(int pos) {
        return memory[pos];
    }

    public void setPosition(int pos, int val) {
        memory[pos] = val;
    }

    public void run() {
        while (ip >= 0 && ip < memory.length) {
            int opcode = getPosition(ip++);
            if (opcode == 99) return;
            int left = getPosition(getPosition(ip++));
            int right = getPosition(getPosition(ip++));
            int dest = getPosition(ip++);
            int ans = switch (opcode) {
                case 1 -> left + right;
                case 2 -> left * right;
                default -> throw new RuntimeException(String.format(
                        "Unknown opcode %s at position %s",
                        opcode,
                        ip - 4));
            };
            setPosition(dest, ans);
        }
    }

}
