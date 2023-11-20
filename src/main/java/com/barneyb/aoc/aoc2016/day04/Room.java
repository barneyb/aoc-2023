package com.barneyb.aoc.aoc2016.day04;

import com.barneyb.aoc.util.Histogram;

import java.util.PriorityQueue;
import java.util.regex.Pattern;

public record Room(String encName, int sector, String chksum, boolean real) {

    private static final Pattern FORMAT = Pattern.compile(
            "([a-z-]+)-([0-9]+)\\[([a-z]+)]");

    public static Room parse(String str) {
        var m = FORMAT.matcher(str);
        if (!m.matches()) throw new RuntimeException(String.format(
                "Failed to parse '%s'",
                str));
        return new Room(m.group(1),
                        Integer.parseInt(m.group(2)),
                        m.group(3),
                        m.group(3).equals(expectedChksum(m.group(1))));
    }

    private static String expectedChksum(String encName) {
        var hist = new Histogram<Character>();
        for (char c : encName.toCharArray()) {
            if (Character.isAlphabetic(c)) hist.count(c);
        }
        var pq = new PriorityQueue<Key>(6);
        hist.forEach((c, l) -> pq.add(new Key(c, l.intValue())));
        return String.valueOf(pq.remove().c) +
                pq.remove().c +
                pq.remove().c +
                pq.remove().c +
                pq.remove().c;
    }

    private record Key(Character c, int n) implements Comparable<Key> {

        @Override
        public int compareTo(Key other) {
            if (n != other.n) return other.n - n;
            return c - other.c;
        }

    }

}
