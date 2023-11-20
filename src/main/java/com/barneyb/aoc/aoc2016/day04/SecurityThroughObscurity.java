package com.barneyb.aoc.aoc2016.day04;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.ArrayList;
import java.util.List;

public class SecurityThroughObscurity extends SolvePartOne<List<Room>, Integer> {

    public static void main(String[] args) {
        new SecurityThroughObscurity().solveAndPrint();
    }

    @Override
    protected List<Room> buildModel(Input input) {
        List<Room> rooms = new ArrayList<>();
        for (String line : input) {
            rooms.add(Room.parse(line));
        }
        return rooms;
    }

    @Override
    protected Integer solvePartOne(List<Room> rooms) {
        int sum = 0;
        for (Room r : rooms) {
            if (r.real()) sum += r.sector();
        }
        return sum;
    }

}
