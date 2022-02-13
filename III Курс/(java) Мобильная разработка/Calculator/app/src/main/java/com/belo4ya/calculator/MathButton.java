package com.belo4ya.calculator;

import android.widget.Button;

import com.belo4ya.calculator.math.MathOperator;

public class MathButton {
    public final Button BTN;
    public final MathOperator OP;

    public MathButton(Button btn, MathOperator op) {
        this.BTN = btn;
        this.OP = op;
    }
}
