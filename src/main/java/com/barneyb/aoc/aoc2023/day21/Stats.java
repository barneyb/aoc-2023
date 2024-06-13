package com.barneyb.aoc.aoc2023.day21;

import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

@ToString
@EqualsAndHashCode
@NoArgsConstructor
@AllArgsConstructor
public class Stats<T> {

    T center;
    T north;
    T south;
    T east;
    T west;
    T northeast;
    T northwest;
    T southeast;
    T southwest;

    boolean isComplete() {
        return north != null
               && south != null
               && east != null
               && west != null
               && northeast != null
               && northwest != null
               && southeast != null
               && southwest != null;
    }

}
