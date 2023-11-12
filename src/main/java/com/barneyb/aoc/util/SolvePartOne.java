package com.barneyb.aoc.util;

import java.util.function.Consumer;

public abstract class SolvePartOne<Model, Answer> extends Solve<Model> {

    protected SolvePartOne(int year, int day) {
        super(year, day);
    }

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        doneWithPart.accept(workInfo(() -> solvePartOne(model)));
    }

    protected abstract Answer solvePartOne(Model model);

}
