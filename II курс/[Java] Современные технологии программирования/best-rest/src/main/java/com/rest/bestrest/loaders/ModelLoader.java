package com.rest.bestrest.loaders;

import com.rest.bestrest.repositories.ClientRepository;
import org.springframework.boot.CommandLineRunner;

public class ModelLoader implements CommandLineRunner {
    private final ClientRepository modelRepository;

    public ModelLoader(ClientRepository clientRepository) {
        this.modelRepository = clientRepository;
    }

    @Override
    public void run(String... args) throws Exception {

    }

}
