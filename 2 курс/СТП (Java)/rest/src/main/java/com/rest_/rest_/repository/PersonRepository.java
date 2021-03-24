package com.rest_.rest_.repository;

import com.rest_.rest_.entity.Person;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;


public interface PersonRepository extends JpaRepository<Person, Long>{
    void delete(Optional<Person> buff);
}
