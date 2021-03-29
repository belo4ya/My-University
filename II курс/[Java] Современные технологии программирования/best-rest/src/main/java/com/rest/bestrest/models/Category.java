package com.rest.bestrest.models;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

import javax.persistence.Entity;
import javax.persistence.ManyToMany;
import java.util.List;

@Entity
@EqualsAndHashCode(callSuper = true)
@Data
@NoArgsConstructor
@ToString
public class Category extends SuperEntity {
    private String title;

    @ManyToMany(mappedBy = "categories")
    private List<Task> tasks;
}
