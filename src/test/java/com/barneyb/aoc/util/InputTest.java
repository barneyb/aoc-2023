package com.barneyb.aoc.util;

import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.util.Iterator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;

class InputTest {

    @Test
    void testToString() {
        Input in = build();
        assertEquals("a\nb", in.toString());
    }

    @Test
    void iterator() {
        Input in = build();
        Iterator<String> itr = in.iterator();
        assertEquals("a", itr.next());
        assertEquals("b", itr.next());
        assertFalse(itr.hasNext());
        //noinspection ConstantValue
        assertFalse(itr.hasNext());
    }

    @Test
    void firstLine() {
        Input in = build();
        assertEquals("a", in.firstLine());
    }

    @Test
    void consumes_lines() {
        Input in = build();
        in.iterator();
        assertThrows(RuntimeException.class, in::iterator);
    }

    @Test
    void consumes_mixed() {
        Input in = build();
        in.firstLine();
        assertThrows(RuntimeException.class, in::toString);
    }

    private static Input build() {
        return new Input(new ByteArrayInputStream("a\nb\n".getBytes()));
    }

}
