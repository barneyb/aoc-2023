package com.barneyb.aoc.util;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.NoSuchElementException;

public final class Input implements Iterable<String> {

    public static Input of(int year, int day) {
        return new Input(year, day);
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

    public String firstLine() {
        return iterator().next();
    }

}
