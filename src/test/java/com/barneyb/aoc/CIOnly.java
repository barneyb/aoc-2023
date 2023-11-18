package com.barneyb.aoc;

import org.junit.jupiter.api.condition.EnabledIfEnvironmentVariable;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@EnabledIfEnvironmentVariable(
        named = "CI",
        matches = "true",
        disabledReason = "Only in CI - too slow")
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.TYPE, ElementType.METHOD })
public @interface CIOnly {
}
