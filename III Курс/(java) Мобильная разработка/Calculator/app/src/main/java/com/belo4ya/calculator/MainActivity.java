package com.belo4ya.calculator;

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

    private Number a = new Number();
    private Number b = new Number();
    private MathOperator op;
    private State state = State.INITIAL;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initViews();

        numericKeyboard.values().forEach(
                kBtn -> kBtn.btn.setOnClickListener(this::handleNumericButtonClick)
        );
        mathKeyboard.values().forEach(
                kBtn -> kBtn.btn.setOnClickListener(this::handleMathButtonClick)
        );
        calculateButton.setOnClickListener(this::handleCalculateButtonClick);
        clearButton.setOnClickListener(this::handleClearButtonClick);
        deleteButton.setOnClickListener(this::handleDeleteButtonClick);
        decimalSepButton.setOnClickListener(this::handleDecimalSepButtonClick);
        signButton.setOnClickListener(this::handleSignButtonClick);
        percentButton.setOnClickListener(this::handlePercentButtonClick);
    }

    private void handleNumericButtonClick(View view) {
        Button btn = (Button) view;
        String digit = Objects.requireNonNull(numericKeyboard.get(btn.getId())).literal;

        if (state == State.INITIAL) {
            if (!digit.equals(Constants.ZERO)) {
                a = new Number(digit);
                state = State.INPUT_FIRST_OPERAND;
                mainTextView.setText(a.toString());
            }
        } else if (state == State.INPUT_FIRST_OPERAND) {
            a.append(digit);
            mainTextView.setText(a.toString());
        } else if (state == State.MATH_OP_IS_SET) {
            b = new Number(digit);
            mainTextView.setText(b.toString());
            state = State.INPUT_SECOND_OPERAND;
        } else if (state == State.INPUT_SECOND_OPERAND) {
            b.append(digit);
            mainTextView.setText(b.toString());
        } else if (state == State.RESULT_IS_CALCULATED) {
            reset();
            a.append(digit);
            state = State.MATH_OP_IS_SET;
        }
    }

    private void handleMathButtonClick(View view) {
        Button btn = (Button) view;
        if (state == State.INPUT_SECOND_OPERAND) {
            a = op.apply(a, b);
            mainTextView.setText(a.toString());
        }
        op = Objects.requireNonNull(mathKeyboard.get(btn.getId())).op;
        subTextView.setText(String.format("%s %s", a, op));
        state = State.MATH_OP_IS_SET;
    }

    private void handleCalculateButtonClick(View view) {
        if (state == State.INPUT_FIRST_OPERAND) {
            subTextView.setText(String.format("%s =", a));
        } else {
            if (b == null) {
                b = a;
            }
            subTextView.setText(String.format("%s %s %s =", a, op, b));
            a = op.apply(a, b);
            mainTextView.setText(a.toString());
            state = State.RESULT_IS_CALCULATED;
        }
    }

    private void handleDecimalSepButtonClick(View view) {

    }

    private void handleClearButtonClick(View view) {
        reset();
    }

    private void handleDeleteButtonClick(View view) {

    }

    private void handleSignButtonClick(View view) {

    }

    private void handlePercentButtonClick(View view) {

    }

    private void reset() {
        state = State.INITIAL;
        a = new Number();
        b = new Number();
        op = null;

        mainTextView.setText(Constants.ZERO);
        subTextView.setText("");
    }

    private void initViews() {
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

        mathKeyboard.put(R.id.add, new MathButton(findViewById(R.id.add), new AddOperator()));
        mathKeyboard.put(R.id.sub, new MathButton(findViewById(R.id.sub), new SubOperator()));
        mathKeyboard.put(R.id.mul, new MathButton(findViewById(R.id.mul), new MulOperator()));
        mathKeyboard.put(R.id.div, new MathButton(findViewById(R.id.div), new DivOperator()));

        calculateButton = findViewById(R.id.calculate);
        clearButton = findViewById(R.id.clear);
        deleteButton = findViewById(R.id.del);
        decimalSepButton = findViewById(R.id.dec_sep);
        signButton = findViewById(R.id.sign);
        percentButton = findViewById(R.id.percent);
    }
}