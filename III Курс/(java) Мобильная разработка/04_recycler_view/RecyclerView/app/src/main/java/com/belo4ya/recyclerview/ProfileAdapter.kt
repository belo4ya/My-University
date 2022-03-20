package com.belo4ya.recyclerview

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ProfileAdapter(private val profiles: List<Profile>) :
    RecyclerView.Adapter<ProfileAdapter.ProfileViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ProfileViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.profile_item, parent, false)
        return ProfileViewHolder(view)
    }

    override fun onBindViewHolder(holder: ProfileViewHolder, position: Int) {
        val profile = profiles[position]
        holder.bind(profile)
        holder.itemView.tag = profile
    }

    override fun getItemCount(): Int {
        return profiles.size
    }

    class ProfileViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val nameTextView: TextView = itemView.findViewById(R.id.name)
        private val avatarImageView: ImageView = itemView.findViewById(R.id.avatar)

        fun bind(profile: Profile) {
            nameTextView.text = itemView.resources.getString(
                R.string.name_template,
                profile.lastName,
                profile.firstName
            )
            avatarImageView.setImageResource(profile.avatar)
        }

    }
}