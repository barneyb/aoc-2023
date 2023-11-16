package com.barneyb.aoc.util;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.time.Month;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

public final class Input implements Iterable<String> {

    private static final int FIRST_YEAR = 2015;
    private static final int FIRST_DAY = 1;
    private static final int LAST_DAY = 25;

    public static Input of(int year, int day) {
        return new Input(year, day);
    }

    /**
     * I interrogate the passed Class's packages' names to identify the year and
     * day it solves, and return the input for that day.
     *
     * @throws NumberFormatException    if the package names don't contain valid
     *                                  year/day numeric strings.
     * @throws IllegalArgumentException if the year/day is not valid
     */
    public static Input of(Class<?> clazz) {
        String[] parts = clazz.getPackageName()
                .split("\\.");
        int year = Integer.parseInt(parts[parts.length - 2].substring(3));
        int day = Integer.parseInt(parts[parts.length - 1].substring(3));
        validateDay(year, day);
        return Input.of(year, day);
    }

    private static void validateDay(int year, int day) {
        ZonedDateTime now = ZonedDateTime.now(ZoneId.of("America/New_York"));
        int maxYear = year == now.getYear() && Month.DECEMBER == now.getMonth()
                ? now.getYear()
                : now.getYear() - 1;
        if (year < FIRST_YEAR || year > maxYear) {
            throw new IllegalArgumentException(String.format(
                    "Year must be %s-%s",
                    FIRST_YEAR,
                    maxYear));
        }
        int maxDay = LAST_DAY;
        if (year == now.getYear()) {
            // already know it's december
            maxDay = Math.min(maxDay, now.getDayOfMonth());
        }
        if (day < FIRST_DAY || day > maxDay) {
            throw new IllegalArgumentException(String.format(
                    "Day must be %s-%s",
                    FIRST_DAY,
                    maxDay));
        }
    }

    /**
     * I create an Input from a literal string. I'm mostly useful for tests.
     */
    public static Input of(String str) {
        return new Input(new ByteArrayInputStream(str.getBytes()));
    }

    private InputStream inStream;

    private Input(int year, int day) {
        String path = String.format("%d/%02d.txt", year, day);
        inStream = Thread.currentThread()
                .getContextClassLoader()
                .getResourceAsStream(path);
        if (inStream == null) {
            throw new RuntimeException("Failed to open input " + path);
        }
    }

    Input(InputStream inStream) {
        this.inStream = inStream;
    }

    private static class Lines implements Iterator<String> {

        private BufferedReader reader;
        private String line;

        public Lines(InputStream inStream) {
            reader = new BufferedReader(
                    new InputStreamReader(inStream));
        }

        @Override
        public boolean hasNext() {
            if (line != null) return true;
            if (reader == null) return false;
            try {
                line = reader.readLine();
            } catch (IOException ioe) {
                throw new RuntimeException("Failed to read from input", ioe);
            }
            boolean hasNext = line != null;
            if (!hasNext) try {
                reader.close();
            } catch (Exception e) {
                new RuntimeException("Failed to close input", e)
                        .printStackTrace(System.err);
            } finally {
                reader = null;
            }
            return hasNext;
        }

        @Override
        public String next() {
            if (!hasNext()) throw new NoSuchElementException();
            String l = line;
            line = null;
            return l;
        }

    }

    @Override
    public Iterator<String> iterator() {
        if (inStream == null) {
            throw new RuntimeException("This input has already been consumed");
        }
        Lines lines = new Lines(inStream);
        inStream = null;
        return lines;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (String line : this) {
            if (!sb.isEmpty()) sb.append('\n');
            sb.append(line);
        }
        return sb.toString();
    }

    public char[] toCharArray() {
        return toString().toCharArray();
    }

    public Stream<String> streamLines() {
        return StreamSupport.stream(spliterator(),
                                    false);
    }

    public String firstLine() {
        return iterator().next();
    }

}
