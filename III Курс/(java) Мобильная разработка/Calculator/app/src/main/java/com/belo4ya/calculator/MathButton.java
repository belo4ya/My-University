package com.belo4ya.calculator;

import android.widget.Button;

import com.belo4ya.calculator.math.MathOperator;

public class MathButton {
    public final Button btn;
    public final MathOperator op;

    public MathButton(Button btn, MathOperator op) {
        this.btn = btn;
        this.op = op;
    }
}
