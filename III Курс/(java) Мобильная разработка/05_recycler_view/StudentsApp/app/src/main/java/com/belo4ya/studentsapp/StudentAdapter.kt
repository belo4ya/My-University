package com.belo4ya.studentsapp

import android.view.*
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView


class StudentAdapter(
    private val students: MutableList<Student>,
    private val clickListener: Listener
) :
    RecyclerView.Adapter<StudentAdapter.StudentViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): StudentViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.student_item, parent, false)
        view.setOnClickListener { v: View ->
            clickListener.onStudentClick(
                v,
                v.tag as Int
            )
        }
        return StudentViewHolder(view)
    }

    override fun onBindViewHolder(holder: StudentViewHolder, position: Int) {
        val student = students[position]
        holder.bind(student)
        holder.itemView.tag = position
    }

    override fun getItemCount(): Int {
        return students.size
    }

    class StudentViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val nameTextView: TextView = itemView.findViewById(R.id.student_item__tv_name)
        private val avatarImageView: ImageView = itemView.findViewById(R.id.student_item__avatar)
        private var student: Student? = null

        fun bind(student: Student) {
            this.student = student

            nameTextView.text = itemView.resources.getString(
                R.string.name_template,
                student.lastName,
                student.firstName
            )
            avatarImageView.setImageResource(student.avatar)
            itemView.setBackgroundColor(itemView.resources.getColor(student.color))
            itemView.setOnCreateContextMenuListener(this::onCreateContextMenu)
        }

        private fun onCreateContextMenu(
            menu: ContextMenu,
            v: View,
            menuInfo: ContextMenu.ContextMenuInfo
        ) {
            val colorRed = menu.add(Menu.NONE, 1, 1, "Primary")
            val colorBlue = menu.add(Menu.NONE, 2, 2, "Accent")
            val colorWhite = menu.add(Menu.NONE, 3, 3, "Очистить")
            colorRed.setOnMenuItemClickListener(onEditMenu)
            colorBlue.setOnMenuItemClickListener(onEditMenu)
            colorWhite.setOnMenuItemClickListener(onEditMenu)
        }

        private val onEditMenu =
            MenuItem.OnMenuItemClickListener { item ->
                when (item.itemId) {
                    1 -> {
                        student!!.color = R.color.colorPrimary
                    }
                    2 -> {
                        student!!.color = R.color.colorAccent
                    }
                    3 -> {
                        student!!.color = R.color.white
                    }
                }
                itemView.setBackgroundColor(itemView.resources.getColor(student!!.color))
                true
            }
    }

    interface Listener {
        fun onStudentClick(view: View?, i: Int)
    }
}