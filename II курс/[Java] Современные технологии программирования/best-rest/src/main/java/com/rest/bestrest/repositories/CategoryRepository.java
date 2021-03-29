package com.rest.bestrest.repositories;

import com.rest.bestrest.models.Category;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CategoryRepository extends JpaRepository<Category, Long> {
}
