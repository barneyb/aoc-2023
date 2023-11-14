package com.barneyb.aoc.util;

import java.util.function.Consumer;

@SuppressWarnings("unused")
public abstract class SolvePartOne<Model, Answer> extends Solve<Model> {

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        doneWithPart.accept(workInfo(() -> solvePartOne(model)));
    }

    @Override
    void test(Model model, Consumer<Object> solutionConsumer) {
        solutionConsumer.accept(solvePartOne(model));
    }

    protected abstract Answer solvePartOne(Model model);

}
