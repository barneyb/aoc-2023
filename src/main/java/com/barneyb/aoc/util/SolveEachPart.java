package com.barneyb.aoc.util;

import java.util.Arrays;
import java.util.function.Consumer;

public abstract class SolveEachPart<Model, AnswerOne, AnswerTwo> extends Solve<Model> {

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        doneWithPart.accept(workInfo(() -> solvePartOne(model)));
        Model partTwoModel;
        if (Arrays.stream(getClass().getAnnotations())
                .anyMatch(a -> a instanceof ConsumesModel)) {
            partTwoModel = buildModel(getInput());
        } else {
            partTwoModel = model;
        }
        doneWithPart.accept(workInfo(() -> solvePartTwo(partTwoModel)));
    }

    @Override
    void test(Model model, Consumer<Object> solutionConsumer) {
        solutionConsumer.accept(solvePartOne(model));
        solutionConsumer.accept(solvePartTwo(model));
    }

    protected abstract AnswerOne solvePartOne(Model model);

    protected abstract AnswerTwo solvePartTwo(Model model);

}
