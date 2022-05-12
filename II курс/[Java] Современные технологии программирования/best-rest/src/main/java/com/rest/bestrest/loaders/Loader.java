package com.rest.bestrest.loaders;

import com.rest.bestrest.models.Client;
import com.rest.bestrest.repositories.ClientRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class Loader implements CommandLineRunner {
    private final ClientRepository clientRepository;

    public Loader(ClientRepository clientRepository) {
        this.clientRepository = clientRepository;
    }

    @Override
    public void run(String... args) throws Exception {
        Client client = new Client();
        client.setUsername("alex");
        client.setFirstName("alexey");
        clientRepository.save(client);
    }

}
