package com.barneyb.aoc.aoc2022.day05;

import java.util.List;

/**
 * I store the initial stacks and moved for the puzzle. The stacks are oriented
 * as if the input file were turns 90 degrees clockwise, and then read into
 * memory. That is, index zero corresponds to the left-most stack, and the first
 * character of the string corresponds to the bottom-most crate.
 */
public record StacksAndMoves(List<String> stacks,
                             List<Move> moves) {
}
