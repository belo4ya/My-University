package com.rest.bestrest.services;

import com.rest.bestrest.models.SuperEntity;
import org.springframework.stereotype.Component;

import java.util.Calendar;

@Component
public class TimeHandler {

    public static void createAndUpdate(SuperEntity superEntity) {
        if (superEntity.getCreationTime() == null) {
            superEntity.setCreationTime(Calendar.getInstance());
        }
        superEntity.setUpdateTime(Calendar.getInstance());
    }
}
