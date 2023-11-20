package com.barneyb.aoc.aoc2017.day07;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class RecursiveCircus extends SolvePartOne<List<Program>, String> {

    public static void main(String[] args) {
        new RecursiveCircus().solveAndPrint();
    }

    @Override
    protected List<Program> buildModel(Input input) {
        List<Program> programs = new ArrayList<>();
        for (String line : input) {
            programs.add(Program.parse(line));
        }
        return programs;
    }

    @Override
    protected String solvePartOne(List<Program> programs) {
        Set<String> candidates = new HashSet<>();
        Set<String> aboves = new HashSet<>();
        for (Program prog : programs) {
            if (prog.isLeaf()) continue;
            if (!aboves.contains(prog.name())) {
                candidates.add(prog.name());
            }
            aboves.addAll(prog.above());
        }
        for (String name : candidates) {
            if (!aboves.contains(name)) return name;
        }
        throw new RuntimeException("Failed to find the root");
    }

}
