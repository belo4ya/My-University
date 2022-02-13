package com.belo4ya.calculator;

import android.widget.Button;

public class NumericButton {
    public final Button btn;
    public final String literal;

    public NumericButton(Button btn, String literal) {
        this.btn = btn;
        this.literal = literal;
    }
}
