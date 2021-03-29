package com.rest.bestrest.assemblers;

import com.rest.bestrest.controllers.CategoryController;
import com.rest.bestrest.models.Category;
import com.sun.istack.NotNull;
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.server.RepresentationModelAssembler;
import org.springframework.stereotype.Component;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.linkTo;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.methodOn;

@Component
public class CategoryAssembler implements RepresentationModelAssembler<Category, EntityModel<Category>> {

    @Override
    public EntityModel<Category> toModel(Category category) {
        return EntityModel.of(category,
                linkTo(methodOn(CategoryController.class).one(category.getId())).withSelfRel(),
                linkTo(methodOn(CategoryController.class).all()).withRel("categories"));
    }
}
