package com.rest.bestrest.repositories;

import com.rest.bestrest.models.Client;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ClientRepository extends JpaRepository<Client, Long> {
}
