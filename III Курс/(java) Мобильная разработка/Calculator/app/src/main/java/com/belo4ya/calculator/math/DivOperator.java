package com.belo4ya.calculator.math;

public class DivOperator extends MathOperator {

    public DivOperator(String s) {
        super(s);
    }

    @Override
    public Number apply(Number a, Number b) {
        return new Number(a.asDouble() / b.asDouble());
    }
}
