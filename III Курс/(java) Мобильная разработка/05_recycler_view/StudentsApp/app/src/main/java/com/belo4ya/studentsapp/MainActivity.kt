package com.belo4ya.studentsapp

import android.os.Bundle
import android.view.View
import android.widget.CheckBox
import android.widget.EditText
import android.widget.ImageView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView


class MainActivity : AppCompatActivity() {
    private var students: MutableList<Student>? = null
    private var studentSurName: EditText? = null
    private var studentName: EditText? = null
    private var gender: CheckBox? = null
    private var avatar: ImageView? = null
    private var index = -1
    private var imageResource = 0
    private var studentAdapter: StudentAdapter? = null
    private var currentView: View? = null
    private var studentLeftBorder: View? = null
    private var studentRightBorder: View? = null
    private var studentTopBorder: View? = null
    private var studentBottomBorder: View? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setupFields()
        setupRecyclerView()
        setupButtons()
    }

    private fun setupButtons() {
        findViewById<View>(R.id.activity_main__save_student_button).setOnClickListener { onSaveClick() }
        findViewById<View>(R.id.activity_main__delete_student_button).setOnClickListener { onDeleteClick() }
        findViewById<View>(R.id.activity_main__add_student_button).setOnClickListener { onAddClick() }
        gender!!.setOnClickListener { onChecked() }
    }

    private fun setupRecyclerView() {
        val recyclerView = findViewById<RecyclerView>(R.id.activity_main__rv_students)
        studentAdapter = StudentAdapter(
            students!!,
            object : StudentAdapter.Listener {
                override fun onStudentClick(view: View?, i: Int) {
                    onStudentClickHandler(view, i)
                }
            }
        )
        recyclerView.adapter = studentAdapter
        val mLayoutManager = LinearLayoutManager(this)
        recyclerView.layoutManager = mLayoutManager
    }

    private fun setupFields() {
        studentSurName = findViewById(R.id.activity_main__studentSurName)
        studentName = findViewById(R.id.activity_main__studentName)
        gender = findViewById(R.id.activity_main__checkGender)
        avatar = findViewById(R.id.activity_main__studentPicture)
        students = generateStudents().toMutableList()
    }

    private fun onAddClick() {
        if (index != -1 && isDataSaved) {
            Toast.makeText(this, R.string.user_should_save_created_warning, Toast.LENGTH_SHORT)
                .show()
        } else {
            val student = Student("", "", 0, true, R.color.white)
            student.avatar = R.drawable.avatar_placeholder
            students!!.add(student)
            studentAdapter!!.notifyDataSetChanged()
            setStudent(null, students!!.size - 1)
        }
    }

    private fun onChecked() {
        imageResource = R.drawable.avatar_placeholder
        avatar!!.setImageResource(imageResource)
    }

    private fun clearData() {
        index = -1
        studentName!!.setText("")
        studentSurName!!.setText("")
        gender!!.isChecked = false
        avatar!!.setImageResource(0)
        studentName!!.error = null
        studentSurName!!.error = null
        setBorderVisibility(currentView, View.INVISIBLE)
    }

    private fun onStudentClickHandler(view: View?, i: Int) {
        if (index != -1) {
            if (checkFields()) {
                if (isDataSaved) {
                    Toast.makeText(this, R.string.user_should_save_warning, Toast.LENGTH_SHORT)
                        .show()
                } else {
                    setStudent(view, i)
                }
            }
        } else {
            setStudent(view, i)
        }
    }

    private val isDataSaved: Boolean
        get() = students!![index].firstName.trim { it <= ' ' }.isEmpty() ||
                students!![index].lastName.trim().isEmpty()

    private fun checkFields(): Boolean {
        if (studentName!!.text.toString().trim { it <= ' ' }
                .isNotEmpty() && studentSurName!!.text.toString().trim { it <= ' ' }.isNotEmpty()
        ) {
            return true
        }
        if (studentName!!.text.toString().trim { it <= ' ' }.isEmpty()) {
            studentName!!.error = resources.getString(R.string.student_first_name_error)
        }
        if (studentSurName!!.text.toString().trim { it <= ' ' }.isEmpty()) {
            studentSurName!!.error = resources.getString(R.string.student_last_name_error)
        }
        return false
    }

    private fun setStudent(view: View?, i: Int) {
        studentSurName!!.setText(students!![i].lastName)
        studentName!!.setText(students!![i].firstName)
        gender!!.isChecked = students!![i].sex == true
        avatar!!.setImageResource(students!![i].avatar)
        index = i
        if (currentView != null) {
            setBorderVisibility(currentView, View.INVISIBLE)
        }
        view?.let { setBorders(it) }
        currentView = view
        setBorderVisibility(view, View.VISIBLE)
        updateButtons(true)
    }

    private fun setBorders(view: View) {
        studentLeftBorder = view.findViewById(R.id.student_item__left)
        studentRightBorder = view.findViewById(R.id.student_item__right)
        studentTopBorder = view.findViewById(R.id.student_item__top)
        studentBottomBorder = view.findViewById(R.id.student_item__bottom)
    }

    private fun updateButtons(value: Boolean) {
        studentName!!.isEnabled = value
        studentSurName!!.isEnabled = value
        gender!!.isEnabled = value
        findViewById<View>(R.id.activity_main__save_student_button).isEnabled = value
        findViewById<View>(R.id.activity_main__delete_student_button).isEnabled = value
    }

    private fun setBorderVisibility(view: View?, visible: Int) {
        if (view != null) {
            studentTopBorder!!.visibility = visible
            studentBottomBorder!!.visibility = visible
            studentLeftBorder!!.visibility = visible
            studentRightBorder!!.visibility = visible
        }
    }

    private fun onSaveClick() {
        if (checkFields()) {
            students!![index].firstName = firstName
            students!![index].lastName = lastName
            students!![index].sex = gender!!.isChecked
            students!![index].avatar = imageResource
            Toast.makeText(this, R.string.student_saved, Toast.LENGTH_SHORT).show()
            students!!.sortBy { s -> s.lastName + s.firstName }
            studentAdapter!!.notifyDataSetChanged()
        }
    }

    private fun onDeleteClick() {
        updateButtons(false)
        students!!.removeAt(index)
        studentAdapter!!.notifyDataSetChanged()
        Toast.makeText(this, R.string.student_removed, Toast.LENGTH_SHORT).show()
        clearData()
    }

    private val firstName: String
        get() = studentName!!.text.toString()

    private val lastName: String
        get() = studentSurName!!.text.toString()
}

private fun generateStudents(): List<Student> {
    return listOf(
        Student("Alexey", "Kovalev", R.drawable.avatar_placeholder, true, R.color.colorAccent),
        Student("Alex", "Kovalev", R.drawable.avatar_placeholder, true),
        Student("Vladimir", "Luter", R.drawable.avatar_placeholder, true),
        Student("Vadim", "Pernyak", R.drawable.avatar_placeholder, true),
    )
}