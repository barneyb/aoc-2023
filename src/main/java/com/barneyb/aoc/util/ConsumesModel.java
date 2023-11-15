package com.barneyb.aoc.util;

import java.lang.annotation.Documented;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * I indicate a {@link SolveEachPart} subtype consumes its model as part of
 * solving part one, so a new instance must be built for solving part two.
 */
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface ConsumesModel {
}
