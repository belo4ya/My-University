package com.rest.bestrest.models;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.MappedSuperclass;
import java.util.Calendar;

@MappedSuperclass
@Data
@NoArgsConstructor
@ToString
public class SuperEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Calendar creationTime;
    private Calendar updateTime;
}
