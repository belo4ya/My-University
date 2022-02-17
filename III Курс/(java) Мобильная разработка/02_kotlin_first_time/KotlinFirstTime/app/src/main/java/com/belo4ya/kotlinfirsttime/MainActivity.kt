package com.belo4ya.kotlinfirsttime

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    private var counter: Int = 0
    private lateinit var counterText: TextView
    private lateinit var nTimesText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        counterText = findViewById(R.id.counter)
        nTimesText = findViewById(R.id.n_times)

        val incrementBtn = findViewById<Button>(R.id.increment)
        incrementBtn.setOnClickListener(fun(_: View?) {
            update(counter + 1)
        })

        val decrementBtn = findViewById<Button>(R.id.decrement)
        decrementBtn.setOnClickListener(fun(_: View?) {
            if (counter > 0) update(counter - 1)
        })

        val resetBtn = findViewById<Button>(R.id.reset)
        resetBtn.setOnClickListener(fun(_: View?) {
            update(0)
        })
    }

    private fun update(n: Int) {
        counter = n
        counterText.text = counter.toString()
        nTimesText.text = resources.getQuantityText(R.plurals.n_times_plurals, counter)
    }
}