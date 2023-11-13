package com.barneyb.aoc.util;

import java.util.function.Consumer;

public abstract class SolveEachPart<Model, AnswerOne, AnswerTwo> extends Solve<Model> {

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        doneWithPart.accept(workInfo(() -> solvePartOne(model)));
        doneWithPart.accept(workInfo(() -> solvePartTwo(model)));
    }

    @Override
    void test(Model model, Consumer<Object> solutionConsumer) {
        solutionConsumer.accept(solvePartOne(model));
        solutionConsumer.accept(solvePartTwo(model));
    }

    protected abstract AnswerOne solvePartOne(Model model);

    protected abstract AnswerTwo solvePartTwo(Model model);

}
