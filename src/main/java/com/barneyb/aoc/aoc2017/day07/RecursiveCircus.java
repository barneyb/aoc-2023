package com.barneyb.aoc.aoc2017.day07;

import com.barneyb.aoc.graph.Digraph;
import com.barneyb.aoc.graph.Topological;
import com.barneyb.aoc.util.Histogram;
import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RecursiveCircus extends SolveEachPart<List<Program>, String, Long> {

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

    @Override
    protected Long solvePartTwo(List<Program> programs) {
        Map<String, Program> programsByName = new HashMap<>();
        var graph = new Digraph<String>();
        for (Program prog : programs) {
            programsByName.put(prog.name(), prog);
            for (String a : prog.above()) {
                graph.addEdge(prog.name(), a);
            }
        }
        Map<String, Long> weightsByName = new HashMap<>();
        for (String name : new Topological<>(graph).reverse()) {
            var prog = programsByName.get(name);
            var totalWeight = prog.weight();
            var subWeights = new Histogram<Long>();
            for (String a : prog.above()) {
                Long w = weightsByName.get(a);
                subWeights.count(w);
                totalWeight += w;
            }
            // can't do this check in the loop above, because if one of the
            // first two sub-towers is the mis-weighted one, we can't tell which
            // until we've checked the third sub-tower.
            if (subWeights.size() > 1) {
                // this is the unbalanced disc!
                Long badWeight = subWeights.bucket(c -> c == 1);
                for (String a : prog.above()) {
                    if (badWeight.equals(weightsByName.get(a))) {
                        // this is the mis-weighted program!
                        Long goodWeight = subWeights.bucket(c -> c != 1);
                        return goodWeight - badWeight + programsByName
                                .get(a)
                                .weight();
                    }
                }
            }
            weightsByName.put(name, totalWeight);
        }
        throw new RuntimeException("Failed to find unbalanced disc");
    }

}
