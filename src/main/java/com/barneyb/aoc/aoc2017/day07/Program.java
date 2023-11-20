package com.barneyb.aoc.aoc2017.day07;

import com.barneyb.aoc.util.PatternUtil;

import java.util.Set;
import java.util.regex.Pattern;

public record Program(String name, long weight, Set<String> above) {

    // fwft (72)
    private static final Pattern FORMAT_LEAF = Pattern.compile(
            "([a-z]+) +\\(([0-9]+)\\)");
    // fwft (72) -> ktlj, cntj, xhth
    private static final Pattern FORMAT_BRANCH = Pattern.compile(
            "([a-z]+) +\\(([0-9]+)\\) +-> +([a-z]+(, +[a-z]+)*)");

    public static Program parse(String str) {
        return str.endsWith(")")
                ? parseLeaf(str)
                : parseBranch(str);
    }

    private static Program parseLeaf(String str) {
        var m = PatternUtil.match(FORMAT_LEAF, str);
        return new Program(m.group(1),
                           Long.parseLong(m.group(2)),
                           Set.of());
    }

    private static Program parseBranch(String str) {
        var m = PatternUtil.match(FORMAT_BRANCH, str);
        return new Program(m.group(1),
                           Long.parseLong(m.group(2)),
                           Set.of(m.group(3).split(", +")));
    }

    public boolean isLeaf() {
        return above.isEmpty();
    }

}
