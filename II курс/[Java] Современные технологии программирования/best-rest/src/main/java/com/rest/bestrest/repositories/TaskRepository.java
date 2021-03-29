package com.rest.bestrest.repositories;

import com.rest.bestrest.models.Task;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TaskRepository extends JpaRepository<Task, Long> {
}
