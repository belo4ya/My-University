package com.belo4ya.calculator.math;

import androidx.annotation.NonNull;

public abstract class MathOperator {
    private final String s;

    public MathOperator(String s) {
        this.s = s;
    }

    public abstract Number apply(Number a, Number b);

    @NonNull
    @Override
    public String toString() {
        return s;
    }
}
