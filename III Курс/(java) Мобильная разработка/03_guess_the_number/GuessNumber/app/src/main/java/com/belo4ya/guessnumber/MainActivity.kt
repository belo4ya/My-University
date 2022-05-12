package com.belo4ya.guessnumber

import android.content.Context
import android.os.Bundle
import android.view.KeyEvent
import android.view.View
import android.view.inputmethod.InputMethodManager
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.textfield.TextInputEditText


class MainActivity : AppCompatActivity() {
    private lateinit var hintView: TextView
    private lateinit var inputView: TextInputEditText
    private lateinit var guessButton: Button

    private val targetNumber: Int = (0..1000).random()
    private var lastNumber: Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initViews()

        inputView.setOnKeyListener(fun(view, i, _): Boolean {
            if (i == KeyEvent.KEYCODE_ENTER) {
                val imm = getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager
                imm.hideSoftInputFromWindow(view.windowToken, 0)
                handleGuessBtnClick(view)
                return true
            }
            return false
        })
        guessButton.setOnClickListener(this::handleGuessBtnClick)
    }

    private fun initViews() {
        hintView = findViewById(R.id.hint)
        inputView = findViewById(R.id.number_input)
        guessButton = findViewById(R.id.guess_btn)
    }

    private fun handleGuessBtnClick(view: View) {
        lastNumber = inputView.text.toString().toInt()
        when {
            lastNumber < targetNumber -> {
                hintView.text = resources.getString(R.string.low)
            }
            lastNumber > targetNumber -> {
                hintView.text = resources.getString(R.string.high)
            }
            else -> {
                hintView.text = resources.getString(R.string.guessed)
            }
        }
    }
}