package com.belo4ya.calculator.math;

import androidx.annotation.NonNull;

public class DivOperator implements MathOperator {
    @Override
    public Number apply(Number a, Number b) {
        return new Number(a.asDouble() / b.asDouble());
    }

    @NonNull
    @Override
    public String toString() {
        return "/";
    }
}
