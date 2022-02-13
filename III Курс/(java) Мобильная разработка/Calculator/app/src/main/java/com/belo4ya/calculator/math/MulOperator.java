package com.belo4ya.calculator.math;

public class MulOperator extends MathOperator {

    public MulOperator(String s) {
        super(s);
    }

    @Override
    public Number apply(Number a, Number b) {
        return new Number(a.asDouble() * b.asDouble());
    }
}
