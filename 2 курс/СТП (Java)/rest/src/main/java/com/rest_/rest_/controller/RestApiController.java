package com.rest_.rest_.controller;

import com.rest_.rest_.entity.Person;
import com.rest_.rest_.service.PersonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
public class RestApiController {

    private final PersonService personService;

    @Autowired
    public RestApiController(PersonService personService){
        this.personService = personService;
    }

    @PostMapping(value = "/api/persons")
    public ResponseEntity<?> create(@RequestBody Person person){
        personService.create(person);
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    @GetMapping(value = "/api/persons")
    public ResponseEntity<List<Person>> findAll(){
        final List<Person> personList = personService.findAll();
        return personList != null && !personList.isEmpty()
                ? new ResponseEntity<>(personList, HttpStatus.OK)
                : new ResponseEntity<>(personList, HttpStatus.NOT_FOUND);
    }

    @GetMapping(value = "/api/persons")
    public ResponseEntity<?> find(@PathVariable(name = "id") Long id){
        final Optional<Person> person = personService.findById(id);
        return person.isPresent()
                ? new ResponseEntity<>(person, HttpStatus.OK)
                : new ResponseEntity<>(person, HttpStatus.NOT_FOUND);
    }

    @PutMapping(value = "/persons/{id}")
    public ResponseEntity<?> update(@PathVariable(name = "id") Long id, @RequestBody Person person) {
        final boolean updated = personService.update(person, id);
        return updated
                ? new ResponseEntity<>(HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    @DeleteMapping(value = "/persons/{id}")
    public ResponseEntity<?> delete(@PathVariable(name = "id") Long id) {
        return personService.delete(id)
                ? new ResponseEntity<>(HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
}
