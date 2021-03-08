package com.spring.simpleapp.repository;

import com.spring.simpleapp.model.Question;
import org.springframework.data.jpa.repository.JpaRepository;

public interface QuestionRepository extends JpaRepository<Question, Long> {
}
