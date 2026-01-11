package com.barneyb.aoc.util;

import lombok.SneakyThrows;

import java.io.File;
import java.io.FileInputStream;

 class TempFileInputSupplier implements InputSupplier {

    private final String path;

    public TempFileInputSupplier(String path) {
        this.path = path;
    }

    public TempFileInputSupplier(File f) {
        this(f.getAbsolutePath());
    }

    @Override
    public void prepare(Solve<?> solve) {
    }

    @SneakyThrows
    @Override
    public Input get() {
        return new Input(new FileInputStream(path));
    }

}
