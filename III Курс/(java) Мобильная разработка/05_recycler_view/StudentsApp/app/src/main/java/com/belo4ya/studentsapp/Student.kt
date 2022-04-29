package com.belo4ya.studentsapp

data class Student(
    var firstName: String,
    var lastName: String,
    var avatar: Int,
    var sex: Boolean,
    var color: Int = R.color.white
)
