package com.belo4ya.calculator;

import android.widget.Button;

public class KeyboardButton {
    public final Button btn;
    public final String literal;

    public KeyboardButton(Button btn, String literal) {
        this.btn = btn;
        this.literal = literal;
    }
}
