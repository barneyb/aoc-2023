package com.barneyb.aoc.util;

import java.util.function.Consumer;

public abstract class SolveEachPart<Model, AnswerOne, AnswerTwo> extends Solve<Model> {

    protected SolveEachPart(int year, int day) {
        super(year, day);
    }

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        doneWithPart.accept(workInfo(() -> solvePartOne(model)));
        doneWithPart.accept(workInfo(() -> solvePartTwo(model)));
    }

    protected abstract AnswerOne solvePartOne(Model model);

    protected abstract AnswerTwo solvePartTwo(Model model);

}
