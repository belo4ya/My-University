package com.belo4ya.calculator.math;

import androidx.annotation.NonNull;

public interface MathOperator {
    public Number apply(Number a, Number b);

    @NonNull
    public String toString();
}
