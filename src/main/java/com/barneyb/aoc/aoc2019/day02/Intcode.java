package com.barneyb.aoc.aoc2019.day02;

import com.barneyb.aoc.util.Input;

import java.util.Arrays;
import java.util.function.Consumer;
import java.util.function.Supplier;

public class Intcode {

    public static int[] parse(Input input) {
        var source = input.toString()
                .split(",");
        var program = new int[source.length];
        for (int i = 0; i < source.length; i++) {
            String s = source[i];
            program[i] = Integer.parseInt(s);
        }
        return program;
    }

    private final int[] memory;
    private Supplier<Integer> stdin;
    private Consumer<Integer> stdout;
    private int ip;
    private int opcode;
    private int modes;

    public Intcode(int[] program) {
        memory = Arrays.copyOf(program, program.length);
    }

    public Intcode(int[] program,
                   Supplier<Integer> stdin,
                   Consumer<Integer> stdout) {
        this(program);
        this.stdin = stdin;
        this.stdout = stdout;
    }

    public int read(int pos) {
        return memory[pos];
    }

    public void write(int pos, int val) {
        memory[pos] = val;
    }

    private void tick() {
        var v = next();
        opcode = v % 100;
        modes = v / 100;
    }

    private int next() {
        return read(ip++);
    }

    private int param() {
        int mode = modes % 10;
        modes /= 10;
        int value = next();
        return switch (mode) {
            case 0 -> read(value);
            case 1 -> value;
            default -> throw new RuntimeException(String.format(
                    "Unknown parameter mode %s at position %s",
                    mode,
                    ip));
        };
    }

    private int input() {
        return stdin.get();
    }

    private void output(int i) {
        stdout.accept(i);
    }

    public void run() {
        while (ip >= 0 && ip < memory.length) {
            tick();
            switch (opcode) {
                case 1: {
                    int a = param();
                    int b = param();
                    write(next(), a + b);
                    break;
                }
                case 2: {
                    int a = param();
                    int b = param();
                    write(next(), a * b);
                    break;
                }
                case 3:
                    write(next(), input());
                    break;
                case 4:
                    output(param());
                    break;
                case 99:
                    return;
                default:
                    throw new RuntimeException(String.format(
                            "Unknown opcode %s at position %s",
                            opcode,
                            ip - 1));
            }
        }
    }

}
