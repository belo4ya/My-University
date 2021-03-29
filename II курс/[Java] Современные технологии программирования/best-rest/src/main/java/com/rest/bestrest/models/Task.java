package com.rest.bestrest.models;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

import javax.persistence.*;
import java.util.Calendar;
import java.util.List;

@Entity
@EqualsAndHashCode(callSuper = true)
@Data
@NoArgsConstructor
@ToString
public class Task extends SuperEntity {
    private String title;
    private String description;
    private Calendar completionDate;
    private boolean isDone;

    @ManyToMany
    private List<Category> categories;

    @ManyToOne
    @JoinColumn(name = "client_id")
    private Client client;
}
