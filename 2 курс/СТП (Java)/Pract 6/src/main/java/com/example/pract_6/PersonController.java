package com.example.pract_6;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class PersonController {

    private final PersonService personService;

    @Autowired
    public PersonController(PersonService personService) {
        this.personService = personService;
    }

    @PostMapping(value = "/persons")
    public ResponseEntity<Person> create(@RequestBody Person person) {
        Person person1 = personService.create(person);
        return new ResponseEntity<>(person1, HttpStatus.CREATED);
    }

    @GetMapping(value = "/persons")
    public ResponseEntity<List<Person>> read() {
        final List<Person> persons = personService.readAll();

        return persons != null && !persons.isEmpty()
                ? new ResponseEntity<>(persons, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    @GetMapping(value = "/persons/{id}")
    public ResponseEntity<Person> read(@PathVariable(name = "id") int id) {
        final Person person = personService.read(id);

        return person != null
                ? new ResponseEntity<>(person, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }

    @PutMapping(value = "/persons/{id}")
    public ResponseEntity<Person> update(@PathVariable(name = "id") int id, @RequestBody Person person) {
        Person person1 = personService.create(person);
        personService.update(person1, id);

        return new ResponseEntity<>(person1, HttpStatus.OK);

    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Person> delete(@RequestParam(value="id") int id){
        personService.delete(id);
        final Person person = personService.read(id);

        return person == null
                ? new ResponseEntity<>(person, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);

    }

}
