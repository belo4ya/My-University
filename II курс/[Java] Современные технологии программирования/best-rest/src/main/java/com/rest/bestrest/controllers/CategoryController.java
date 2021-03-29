package com.rest.bestrest.controllers;

import com.rest.bestrest.assemblers.CategoryAssembler;
import com.rest.bestrest.models.Category;
import com.rest.bestrest.repositories.CategoryRepository;
import com.rest.bestrest.services.TimeHandler;
import org.springframework.data.rest.webmvc.RepositoryRestController;
import org.springframework.data.rest.webmvc.ResourceNotFoundException;
import org.springframework.hateoas.CollectionModel;
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.IanaLinkRelations;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Calendar;
import java.util.List;
import java.util.stream.Collectors;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.linkTo;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.methodOn;

@RepositoryRestController
public class CategoryController {
    private final CategoryRepository repository;
    private final CategoryAssembler assembler;

    public CategoryController(CategoryRepository repository, CategoryAssembler assembler) {
        this.repository = repository;
        this.assembler = assembler;
    }

    @GetMapping("/categories/{id}")
    public ResponseEntity<?> one(@PathVariable Long id) {
        Category category = repository.findById(id).orElseThrow(ResourceNotFoundException::new);
        return ResponseEntity.ok(assembler.toModel(category));
    }

    @GetMapping("/categories")
    public ResponseEntity<?> all() {
        List<EntityModel<Category>> category = repository.findAll().stream()
                .map(assembler::toModel)
                .collect(Collectors.toList());

        return ResponseEntity.ok(CollectionModel.of(category, linkTo(methodOn(CategoryController.class).all()).withSelfRel()));
    }

    @PostMapping("/categories")
    public ResponseEntity<?> createCategory(@RequestBody Category newCategory) {
        TimeHandler.createAndUpdate(newCategory);

        EntityModel<Category> entityModel = assembler.toModel(repository.save(newCategory));
        return ResponseEntity.created(entityModel.getRequiredLink(IanaLinkRelations.SELF).toUri()).body(entityModel);
    }

    @PutMapping("/categories/{id}")
    public ResponseEntity<?> replaceCategory(@RequestBody Category newCategory, @PathVariable Long id) {
        Category updatedCategory = repository.findById(id)
                .map(category -> {
                    category.setTitle(newCategory.getTitle());
                    category.setTasks(newCategory.getTasks());
                    category.setCreationTime(
                            newCategory.getCreationTime() != null ? newCategory.getCreationTime() : Calendar.getInstance()
                    );
                    category.setUpdateTime(
                            newCategory.getUpdateTime() != null ? newCategory.getUpdateTime() : Calendar.getInstance()
                    );
                    return repository.save(category);
                })
                .orElseGet(() -> {
                    newCategory.setId(id);
                    newCategory.setCreationTime(Calendar.getInstance());
                    newCategory.setUpdateTime(Calendar.getInstance());
                    return repository.save(newCategory);
                });

        EntityModel<Category> entityModel = assembler.toModel(updatedCategory);

        return ResponseEntity.created(entityModel.getRequiredLink(IanaLinkRelations.SELF).toUri()).body(entityModel);
    }
}
