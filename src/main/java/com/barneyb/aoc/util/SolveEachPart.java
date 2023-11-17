package com.barneyb.aoc.util;

import java.util.Arrays;
import java.util.function.Consumer;

public abstract class SolveEachPart<Model, AnswerOne, AnswerTwo> extends Solve<Model> {

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        doneWithPart.accept(workInfo(() -> solvePartOne(model)));
        Model partTwoModel = getPartTwoModel(model);
        doneWithPart.accept(workInfo(() -> solvePartTwo(partTwoModel)));
    }

    private Model getPartTwoModel(Model model) {
        Model partTwoModel;
        if (Arrays.stream(getClass().getAnnotations())
                .anyMatch(a -> a instanceof ConsumesModel)) {
            partTwoModel = buildModel(getInput());
        } else {
            partTwoModel = model;
        }
        return partTwoModel;
    }

    @Override
    void test(Model model, Consumer<Object> solutionConsumer) {
        solutionConsumer.accept(solvePartOne(model));
        Model partTwoModel = getPartTwoModel(model);
        solutionConsumer.accept(solvePartTwo(partTwoModel));
    }

    protected abstract AnswerOne solvePartOne(Model model);

    protected abstract AnswerTwo solvePartTwo(Model model);

}
