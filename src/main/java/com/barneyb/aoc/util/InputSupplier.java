package com.barneyb.aoc.util;

import java.util.function.Supplier;

interface InputSupplier extends Supplier<Input> {

    void prepare(Solve<?> solve);

}
