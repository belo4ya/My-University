package com.rest.bestrest.models;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

import javax.persistence.Entity;
import javax.persistence.OneToMany;
import java.util.Date;
import java.util.List;

@Entity
@EqualsAndHashCode(callSuper = true)
@Data
@NoArgsConstructor
@ToString
public class Client extends SuperEntity {
    private String username;
    private String firstName;
    private String lastName;
    private String middleName;
    private Date birthDate;

    @OneToMany(mappedBy = "client")
    private List<Task> tasks;
}
