package com.rest_.rest_.service;

import com.rest_.rest_.entity.Person;
import com.rest_.rest_.repository.PersonRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class PersonService {
    @Autowired
    private PersonRepository personRepository;

    public void create(Person person) {
        personRepository.save(person);
    }

    public List<Person> findAll() {
        return personRepository.findAll();
    }

    public Optional<Person> findById(Long id) {
        return personRepository.findById(id);
    }

    public boolean delete(Long id) {
        Optional<Person> buff = personRepository.findById(id);
        if (buff != null) {
            personRepository.delete(buff);
            return true;
        }
        return false;
    }

    public boolean update(Person person, Long id) {
        Optional<Person> buff = personRepository.findById(id);
        if (buff == null) {
            return false;
        }
        personRepository.delete(buff);
        personRepository.save(person);
        return true;
    }
}