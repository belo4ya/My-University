package com.belo4ya.calculator;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.belo4ya.calculator.math.MathOperator;
import com.belo4ya.calculator.math.Number;

import java.util.HashMap;
import java.util.Objects;

public class MainActivity extends AppCompatActivity {
    private TextView subTextView;
    private TextView mainTextView;
    private HashMap<Integer, KeyboardButton> numericButtons = new HashMap<>();
    private HashMap<Integer, KeyboardButton> binOperationButtons = new HashMap<>();
    private Button calculateButton;
    private Button clearButton;
    private Button deleteButton;
    private Button decimalSepButton;
    private Button signButton;
    private Button percentButton;

    private byte state = 0;  // 1, 2, 3

    private Number a = new Number();
    private Number b;
    private MathOperator op;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initViews();

        for (Button btn : stringsNumericButtons.values()) {
            btn.setOnClickListener(this::handleNumericButtonClick);
        }

        for (Button btn : mathOperationButtons.values()) {
            btn.setOnClickListener(this::handleMathButtonClick);
        }

        Button clearBtn = findViewById(R.id.clear);
        clearBtn.setOnClickListener(this::handleClearButtonClick);

        Button calculateBtn = findViewById(R.id.calculate);
        calculateBtn.setOnClickListener(this::handleCalculateButtonClick);
    }

    private void handleNumericButtonClick(View view) {
        Button btn = (Button) view;
        String digit = btn.getText().toString();

        if (mainTextView.getText().toString().equals(Constants.ZERO) && digit.equals(Constants.ZERO)) {
            return;
        }

        if (state == 0) {
            a.append(digit);
            mainTextView.setText(a.toString());
        } else if (state == 1) {
            b = new Number(digit);
            mainTextView.setText(b.toString());
            state = 2;
        } else if (state == 2) {
            b.append(digit);
            mainTextView.setText(b.toString());
        } else {
            a = new Number(digit);
            mainTextView.setText(a.toString());
            subTextView.setText("");
            state = 1;
        }
    }

    private void handleMathButtonClick(View view) {
        Button btn = (Button) view;
        if (state == 2) {
            a = op.apply(a, b);
            mainTextView.setText(a.toString());
        }
        op = Objects.requireNonNull(operators.get(btn.getId()));
        subTextView.setText(String.format("%s %s", a, op));
        state = 1;
    }

    private void handleCalculateButtonClick(View view) {
        if (state == 0) {
            subTextView.setText(String.format("%s =", a));
        } else {
            if (b == null) {
                b = a;
            }
            subTextView.setText(String.format("%s %s %s =", a, op, b));
            a = op.apply(a, b);
            mainTextView.setText(a.toString());
            state = 3;
        }
    }

    private void handleDecimalSepButtonClick(View view) {

    }

    private void handleClearButtonClick(View view) {
        state = 0;
        a = new Number();
        b = null;
        op = null;

        mainTextView.setText(a.toString());
        subTextView.setText("");
    }

    private void initViews() {

        numericButtons.put(R.id.zero, new KeyboardButton(findViewById(R.id.zero), Constants.ZERO));
        numericButtons.put(R.id.one, new KeyboardButton(findViewById(R.id.one), Constants.ONE));
        numericButtons.put(R.id.two, new KeyboardButton(findViewById(R.id.two), Constants.TWO));
        numericButtons.put(R.id.three, new KeyboardButton(findViewById(R.id.three), Constants.THREE));
        numericButtons.put(R.id.four, new KeyboardButton(findViewById(R.id.four), Constants.FOUR));
        numericButtons.put(R.id.five, new KeyboardButton(findViewById(R.id.five), Constants.FIVE));
        numericButtons.put(R.id.six, new KeyboardButton(findViewById(R.id.six), Constants.SIX));
        numericButtons.put(R.id.seven, new KeyboardButton(findViewById(R.id.seven), Constants.SEVEN));
        numericButtons.put(R.id.eight, new KeyboardButton(findViewById(R.id.eight), Constants.EIGHT));
        numericButtons.put(R.id.nine, new KeyboardButton(findViewById(R.id.nine), Constants.NINE));


        binOperationButtons.put(R.id.add, new KeyboardButton(findViewById(R.id.add), Constants.ADD));
        binOperationButtons.put(R.id.sub, new KeyboardButton(findViewById(R.id.sub), Constants.SUB));
        binOperationButtons.put(R.id.mul, new KeyboardButton(findViewById(R.id.mul), Constants.MUL));
        binOperationButtons.put(R.id.div, new KeyboardButton(findViewById(R.id.div), Constants.DIV));

        subTextView = findViewById(R.id.subText);
        mainTextView = findViewById(R.id.mainText);
    }
}