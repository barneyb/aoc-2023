package com.barneyb.aoc.util;

import lombok.SneakyThrows;

import javax.annotation.Nonnull;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

public final class Input implements Iterable<String>, AutoCloseable {

    /**
     * I create an Input from a literal string. I'm mostly useful for tests.
     */
    public static Input of(String str) {
        return new Input(new ByteArrayInputStream(str.getBytes()));
    }

    private InputStream inStream;

    Input(InputStream inStream) {
        this.inStream = inStream;
    }

    @SneakyThrows
    @Override
    public void close() {
        if (inStream != null) {
            inStream.close();
            inStream = null;
        }
    }

    private static class Lines implements Iterator<String>, AutoCloseable {

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

        @SneakyThrows
        @Override
        public void close() {
            if (reader != null) {
                reader.close();
                reader = null;
            }
        }

    }

    @Nonnull
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
