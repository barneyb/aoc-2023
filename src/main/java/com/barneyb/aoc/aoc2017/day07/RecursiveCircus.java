package com.barneyb.aoc.aoc2017.day07;

import com.barneyb.aoc.graph.Digraph;
import com.barneyb.aoc.graph.Topological;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolvePartOne;

import java.util.ArrayList;
import java.util.List;

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
        var graph = new Digraph<String>();
        for (Program prog : programs) {
            for (String a : prog.above()) {
                graph.addEdge(prog.name(), a);
            }
        }
        return new Topological<>(graph)
                .iterator()
                .next();
    }

}
