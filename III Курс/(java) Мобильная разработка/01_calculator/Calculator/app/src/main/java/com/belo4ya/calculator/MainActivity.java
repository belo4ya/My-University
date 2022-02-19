package com.belo4ya.calculator;

import android.content.res.Resources;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.belo4ya.calculator.math.AddOperator;
import com.belo4ya.calculator.math.DivOperator;
import com.belo4ya.calculator.math.MathOperator;
import com.belo4ya.calculator.math.MulOperator;
import com.belo4ya.calculator.math.Number;
import com.belo4ya.calculator.math.SubOperator;

import java.util.HashMap;
import java.util.Objects;

public class MainActivity extends AppCompatActivity {
    private TextView subTextView;
    private TextView mainTextView;
    private final HashMap<Integer, NumericButton> numericKeyboard = new HashMap<>();
    private final HashMap<Integer, MathButton> mathKeyboard = new HashMap<>();
    private Button calculateButton;
    private Button clearButton;
    private Button deleteButton;
    private Button decimalSepButton;
    private Button signButton;
    private Button percentButton;

    private Number a;
    private Number b;
    private MathOperator op;
    private State state;

    public enum State {
        INITIAL,
        INPUT_FIRST_OPERAND,
        INPUT_SECOND_OPERAND,
        MATH_OP_IS_SET,
        RESULT_IS_NOT_CALCULATED,
        RESULT_IS_CALCULATED,
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initViews();
        reset();

        numericKeyboard.values().forEach(b -> b.BTN.setOnClickListener(this::handleNumericButtonClick));
        mathKeyboard.values().forEach(b -> b.BTN.setOnClickListener(this::handleMathButtonClick));
        calculateButton.setOnClickListener(this::handleCalculateButtonClick);
        clearButton.setOnClickListener(this::handleClearButtonClick);
        deleteButton.setOnClickListener(this::handleDeleteButtonClick);
        decimalSepButton.setOnClickListener(this::handleDecimalSepButtonClick);
        signButton.setOnClickListener(this::handleSignButtonClick);
        percentButton.setOnClickListener(this::handlePercentButtonClick);
    }

    private void handleNumericButtonClick(View view) {
        String digit = Objects.requireNonNull(numericKeyboard.get(view.getId())).LITERAL;

        if (state == State.INITIAL) {
            if (!digit.equals(Constants.ZERO)) {
                a = new Number(digit);
                mainTextView.setText(a.asInString());
                state = State.INPUT_FIRST_OPERAND;
            }
        } else if (state == State.INPUT_FIRST_OPERAND) {
            if (mainTextView.getText().equals(Constants.ZERO)) {
                a = new Number(digit);
            } else {
                a.append(digit);
            }
            mainTextView.setText(a.asInString());
        } else if (state == State.MATH_OP_IS_SET) {
            b = new Number(digit);
            mainTextView.setText(b.asInString());
            state = State.INPUT_SECOND_OPERAND;
        } else if (state == State.INPUT_SECOND_OPERAND) {
            if (mainTextView.getText().equals(Constants.ZERO)) {
                b = new Number(digit);
            } else {
                b.append(digit);
            }
            mainTextView.setText(b.asInString());
        } else if (state == State.RESULT_IS_NOT_CALCULATED) {
            a = new Number(digit);
            mainTextView.setText(a.asInString());
            state = State.INPUT_FIRST_OPERAND;
        } else if (state == State.RESULT_IS_CALCULATED) {
            a = new Number(digit);
            mainTextView.setText(a.asInString());
            subTextView.setText("");
            state = State.MATH_OP_IS_SET;
        }
    }

    private void handleMathButtonClick(View view) {
        if (state == State.INPUT_SECOND_OPERAND) {
            a = op.apply(a, b);
            mainTextView.setText(a.asOutString());
        }
        op = Objects.requireNonNull(mathKeyboard.get(view.getId())).OP;
        subTextView.setText(String.format("%s %s", a.asOutString(), op));
        b = new Number(a);
        state = State.MATH_OP_IS_SET;
    }

    private void handleCalculateButtonClick(View view) {
        if (state == State.INITIAL || state == State.INPUT_FIRST_OPERAND) {
            subTextView.setText(String.format("%s =", a.asOutString()));
            state = State.RESULT_IS_NOT_CALCULATED;
        } else {
            subTextView.setText(String.format("%s %s %s =", a.asOutString(), op, b.asOutString()));
            a = op.apply(a, b);
            mainTextView.setText(a.asOutString());
            state = State.RESULT_IS_CALCULATED;
        }
    }

    private void handleDecimalSepButtonClick(View view) {
        if (state == State.INITIAL || state == State.RESULT_IS_NOT_CALCULATED) {
            a = new Number();
            a.append(Constants.DEC_SEP);
            mainTextView.setText(a.asInString());
            state = State.INPUT_FIRST_OPERAND;
        } else if (state == State.INPUT_FIRST_OPERAND) {
            if (a.isInteger()) {
                a.append(Constants.DEC_SEP);
                mainTextView.setText(a.asInString());
            }
        } else if (state == State.MATH_OP_IS_SET) {
            b = new Number();
            b.append(Constants.DEC_SEP);
            mainTextView.setText(b.asInString());
            state = State.INPUT_SECOND_OPERAND;
        } else if (state == State.INPUT_SECOND_OPERAND) {
            if (b.isInteger()) {
                b.append(Constants.DEC_SEP);
                mainTextView.setText(b.asInString());
            }
        } else if (state == State.RESULT_IS_CALCULATED) {
            a = new Number();
            a.append(Constants.DEC_SEP);
            mainTextView.setText(a.asInString());
            subTextView.setText("");
            state = State.INPUT_FIRST_OPERAND;
        }
    }

    private void handleClearButtonClick(View view) {
        reset();
    }

    private void handleDeleteButtonClick(View view) {
        if (state == State.INPUT_FIRST_OPERAND || state == State.MATH_OP_IS_SET) {
            a.delete();
            mainTextView.setText(a.asInString());
        } else if (state == State.INPUT_SECOND_OPERAND) {
            b.delete();
            mainTextView.setText(b.asInString());
        }
    }

    private void handleSignButtonClick(View view) {
        if (state == State.INPUT_FIRST_OPERAND || state == State.RESULT_IS_NOT_CALCULATED) {
            a.sign();
            mainTextView.setText(a.asOutString());
        } else if (state == State.INPUT_SECOND_OPERAND) {
            b.sign();
            mainTextView.setText(b.asOutString());
        } else if (state == State.RESULT_IS_CALCULATED) {
            a.sign();
            mainTextView.setText(a.asOutString());
            subTextView.setText(a.asOutString());
            state = State.INPUT_FIRST_OPERAND;
        }
    }

    private void handlePercentButtonClick(View view) {
        if (state == State.MATH_OP_IS_SET || state == State.INPUT_SECOND_OPERAND) {
            b = new Number(a.asDouble() * b.asDouble() / 100);
            subTextView.setText(String.format("%s %s %s =", a.asOutString(), op, b.asOutString()));
            a = op.apply(a, b);
            mainTextView.setText(a.asOutString());
            state = State.RESULT_IS_CALCULATED;
        }
    }

    private void reset() {
        state = State.INITIAL;
        a = new Number();
        b = null;
        op = null;

        mainTextView.setText(Constants.ZERO);
        subTextView.setText("");
    }

    private void initViews() {
        Resources resources = getResources();
        subTextView = findViewById(R.id.subText);
        mainTextView = findViewById(R.id.mainText);

        numericKeyboard.put(R.id.zero, new NumericButton(findViewById(R.id.zero), Constants.ZERO));
        numericKeyboard.put(R.id.one, new NumericButton(findViewById(R.id.one), Constants.ONE));
        numericKeyboard.put(R.id.two, new NumericButton(findViewById(R.id.two), Constants.TWO));
        numericKeyboard.put(R.id.three, new NumericButton(findViewById(R.id.three), Constants.THREE));
        numericKeyboard.put(R.id.four, new NumericButton(findViewById(R.id.four), Constants.FOUR));
        numericKeyboard.put(R.id.five, new NumericButton(findViewById(R.id.five), Constants.FIVE));
        numericKeyboard.put(R.id.six, new NumericButton(findViewById(R.id.six), Constants.SIX));
        numericKeyboard.put(R.id.seven, new NumericButton(findViewById(R.id.seven), Constants.SEVEN));
        numericKeyboard.put(R.id.eight, new NumericButton(findViewById(R.id.eight), Constants.EIGHT));
        numericKeyboard.put(R.id.nine, new NumericButton(findViewById(R.id.nine), Constants.NINE));

        mathKeyboard.put(R.id.add, new MathButton(findViewById(R.id.add), new AddOperator(resources.getString(R.string.add))));
        mathKeyboard.put(R.id.sub, new MathButton(findViewById(R.id.sub), new SubOperator(resources.getString(R.string.sub))));
        mathKeyboard.put(R.id.mul, new MathButton(findViewById(R.id.mul), new MulOperator(resources.getString(R.string.mul))));
        mathKeyboard.put(R.id.div, new MathButton(findViewById(R.id.div), new DivOperator(resources.getString(R.string.div))));

        calculateButton = findViewById(R.id.calculate);
        clearButton = findViewById(R.id.clear);
        deleteButton = findViewById(R.id.del);
        decimalSepButton = findViewById(R.id.dec_sep);
        signButton = findViewById(R.id.sign);
        percentButton = findViewById(R.id.percent);
    }
}