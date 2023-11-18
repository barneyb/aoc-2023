package com.barneyb.aoc.aoc2022.day05;

import com.barneyb.aoc.util.Input;
import com.barneyb.aoc.util.SolveEachPart;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class SupplyStacks extends SolveEachPart<StacksAndMoves, String, String> {

    public static void main(String[] args) {
        new SupplyStacks().solveAndPrint();
    }

    @Override
    protected StacksAndMoves buildModel(Input input) {
        var itr = input.iterator();
        // lop off the stack lines, reversing their order, so the labels are
        // on top, and the crates are in "push down orientation" (vs the "pile
        // up orientation" of the input file.
        Deque<String> stackLines = new ArrayDeque<>();
        while (itr.hasNext()) {
            String line = itr.next();
            if (line.isEmpty()) break;
            stackLines.addFirst(line);
        }
        List<Move> moves = new ArrayList<>();
        itr.forEachRemaining(l -> moves.add(Move.parse(l)));
        return new StacksAndMoves(
                parseStacks(stackLines),
                moves);
    }

    private List<String> parseStacks(Deque<String> lines) {
        char[] labels = lines.removeFirst().toCharArray();
        var stacks = new ArrayList<String>();
        // each non-whitespace char in the label row corresponds to a stack, and
        // all its crates are in the same character position of the subsequent
        // lines (which are in "push-down orientation"). As soon as a given line
        // doesn't have a crate label, the stack has been fully read, so break.
        for (int i = 0; i < labels.length; i++) {
            char l = labels[i];
            if (l == ' ') continue;
            var sb = new StringBuilder();
            for (String line : lines) {
                if (i >= line.length()) break;
                char c = line.charAt(i);
                if (c == ' ') break;
                sb.append(c);
            }
            stacks.add(sb.toString());
        }
        return stacks;
    }

    @Override
    protected String solvePartOne(StacksAndMoves model) {
        List<Deque<Character>> stacks = constructStacks(model.stacks());
        for (Move move : model.moves()) {
            var from = stacks.get(move.from() - 1);
            var to = stacks.get(move.to() - 1);
            for (int i = move.count(); i > 0; i--) {
                to.addFirst(from.removeFirst());
            }
        }
        return readTopCrates(stacks);
    }

    @Override
    protected String solvePartTwo(StacksAndMoves model) {
        List<Deque<Character>> stacks = constructStacks(model.stacks());
        for (Move move : model.moves()) {
            var from = stacks.get(move.from() - 1);
            Deque<Character> temp = new ArrayDeque<>();
            for (int i = move.count(); i > 0; i--) {
                temp.addFirst(from.removeFirst());
            }
            // no need to actually remove them from temp
            temp.forEach(stacks.get(move.to() - 1)::addFirst);
        }
        return readTopCrates(stacks);
    }

    private List<Deque<Character>> constructStacks(List<String> model) {
        List<Deque<Character>> stacks = new ArrayList<>(model.size());
        for (String str : model) {
            Deque<Character> stack = new ArrayDeque<>();
            for (char c : str.toCharArray()) {
                stack.addFirst(c);
            }
            stacks.add(stack);
        }
        return stacks;
    }

    private static String readTopCrates(List<Deque<Character>> stacks) {
        var sb = new StringBuilder();
        for (Deque<Character> stack : stacks) {
            sb.append(stack.peekFirst());
        }
        return sb.toString();
    }

}
