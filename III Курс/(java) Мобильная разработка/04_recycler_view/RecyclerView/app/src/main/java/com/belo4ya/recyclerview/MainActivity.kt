package com.belo4ya.recyclerview

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {
    private val profiles = generateProfiles().toMutableList()
    private val profileAdapter = ProfileAdapter(profiles)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val profilesRecyclerView = findViewById<RecyclerView>(R.id.profiles_list)
        profilesRecyclerView.adapter = profileAdapter
        profilesRecyclerView.layoutManager = LinearLayoutManager(this)
    }
}

private fun generateProfiles(): List<Profile> {
    return listOf(
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
        Profile("Алексей", "Ковалев", R.drawable.avatar_placeholder, ""),
    )
}