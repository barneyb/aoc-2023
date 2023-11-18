package com.barneyb.aoc.util;

import java.util.Arrays;
import java.util.Iterator;
import java.util.function.Consumer;
import java.util.stream.Stream;

public abstract class SolveEachPart<Model, AnswerOne, AnswerTwo> extends Solve<Model> {

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        doneWithPart.accept(workInfo(() -> solvePartOne(model)));
        Model partTwoModel = getPartTwoModel(model);
        doneWithPart.accept(workInfo(() -> solvePartTwo(partTwoModel)));
    }

    private Model getPartTwoModel(Model model) {
        Model partTwoModel;
        // streams and iterators are always consumed
        if (model instanceof Stream
                || model instanceof Iterator
                || isConsumesModel()) {
            partTwoModel = buildModel(getInput());
        } else {
            partTwoModel = model;
        }
        return partTwoModel;
    }

    private boolean isConsumesModel() {
        return Arrays.stream(getClass().getAnnotations())
                .anyMatch(a -> a instanceof ConsumesModel);
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
