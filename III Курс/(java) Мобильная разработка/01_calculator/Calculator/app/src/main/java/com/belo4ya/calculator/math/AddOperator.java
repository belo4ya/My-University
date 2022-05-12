package com.belo4ya.calculator.math;

public class AddOperator extends MathOperator {

    public AddOperator(String s) {
        super(s);
    }

    @Override
    public Number apply(Number a, Number b) {
        return new Number(a.asDouble() + b.asDouble());
    }
}
