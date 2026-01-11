package com.barneyb.aoc.util;

import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileOutputStream;

@Slf4j
class AocAllTest {

    @Test
    void support() {
        AocAll.main(new String[]{ "support" });
    }

    @Test
    @SneakyThrows
    void solve() {
        var f = File.createTempFile("input_2015_01", ".txt");
        f.deleteOnExit();
        try ( var out = new FileOutputStream(f)){
            out.write("()())".getBytes());
        }
        AocAll.main(new String[]{"solve", "2015", "1", f.getAbsolutePath()});
        if (!f.delete()) System.err.println("Failed to delete '" + f + "' after test.");
    }

}
