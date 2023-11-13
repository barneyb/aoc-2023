package com.barneyb.aoc.util;

import java.util.Objects;
import java.util.function.Consumer;

public abstract class SolvePartOne<Model, Answer> extends Solve<Model> {

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        doneWithPart.accept(workInfo(() -> solvePartOne(model)));
    }

    protected abstract Answer solvePartOne(Model model);

    public void test(Answer partOne) {
        Model model = buildModel(getInput());
        Answer actual = solvePartOne(model);
        assert Objects.equals(partOne, actual);
    }

}
