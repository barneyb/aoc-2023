package com.barneyb.aoc.util;

import java.util.function.Consumer;

public abstract class SolveTogether<Model, AnswerOne, AnswerTwo> extends Solve<Model> {

    @Override
    void solve(Model model, Consumer<Info<?>> doneWithPart) {
        Info<Answers<AnswerOne, AnswerTwo>> a = workInfo(() -> solveTogether(model));
        doneWithPart.accept(a.map(Answers::partOne));
        doneWithPart.accept(new Info<>(a.result().partTwo()));
    }

    @Override
    void test(Model model, Consumer<Object> solutionConsumer) {
        Answers<AnswerOne, AnswerTwo> a = solveTogether(model);
        solutionConsumer.accept(a.partOne());
        solutionConsumer.accept(a.partTwo());
    }

    protected abstract Answers<AnswerOne, AnswerTwo> solveTogether(Model model);

}
