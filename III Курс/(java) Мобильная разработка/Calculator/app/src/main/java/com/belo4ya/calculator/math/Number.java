package com.belo4ya.calculator.math;

import android.icu.text.DecimalFormat;

import com.belo4ya.calculator.Constants;

public class Number {
    private StringBuilder buff;
    private final DecimalFormat format = new DecimalFormat(Constants.ZERO);

    {
        format.setMaximumFractionDigits(16);
    }

    public Number() {
        buff = new StringBuilder(Constants.ZERO);
    }

    public Number(String s) {
        buff = new StringBuilder(s);
    }

    public Number(Double d) {
        buff = new StringBuilder(d.toString());
    }

    public Number(Number n) {
        buff = n.buff;
    }

    public void append(String s) {
        buff.append(s);
    }

    public void delete() {
        if (buff.length() > 1) {
            buff.setLength(buff.length() - 1);
        } else {
            buff = new StringBuilder(Constants.ZERO);
        }
    }

    public boolean isInteger() {
        return buff.indexOf(Constants.DEC_SEP) == -1;
    }

    public void sign() {
        buff = new StringBuilder(Double.toString(-1 * this.asDouble()));
    }

    public Double asDouble() {
        return Double.valueOf(buff.toString());
    }

    public String asInString() {
        return buff.toString();
    }

    public String asOutString() {
        return format.format(asDouble());
    }
}
