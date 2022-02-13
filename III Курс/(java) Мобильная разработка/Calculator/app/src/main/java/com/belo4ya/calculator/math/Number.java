package com.belo4ya.calculator.math;

import android.icu.text.DecimalFormat;

import androidx.annotation.NonNull;

public class Number {
    private final StringBuffer buff;
    private final DecimalFormat format = new DecimalFormat("0");

    {
        format.setMaximumFractionDigits(16);
    }

    public Number() {
        buff = new StringBuffer("0");
    }

    public Number(String s) {
        buff = new StringBuffer(s);
    }

    public Number(Double d) {
        buff = new StringBuffer(d.toString());
    }

    public void append(String s) {
        buff.append(s);
    }

    public Double asDouble() {
        return Double.valueOf(buff.toString());
    }

    @NonNull
    public String toString() {
        return format.format(Double.valueOf(buff.toString()));
    }
}
