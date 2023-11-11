package com.barneyb.aoc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;

public class Main {

    public static void main(String[] args) {
        String input;
        try (BufferedReader in = new BufferedReader(
                new InputStreamReader(Objects.requireNonNull(
                        Thread.currentThread()
                                .getContextClassLoader()
                                .getResourceAsStream("2015/01.txt"))))) {
            input = in.readLine();
        } catch (IOException ioe) {
            throw new RuntimeException(ioe);
        }
        int floor = 0;
        int bPos = 0;
        char[] chars = input.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (c == '(') floor++;
            else if (c == ')') floor--;
            else throw new RuntimeException(String.format(
                        "Unrecognized '%s'",
                        c));
            if (floor == -1 && bPos == 0) bPos = i + 1;
        }
        System.out.println(floor);
        System.out.println(bPos);
    }

}
