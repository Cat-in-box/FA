package com.example.pract_6;

public class Person {
    private Integer id;
    private String firstName;
    private String lastName;
    private String city;
    private String street;

    public String getStreet() {
        return street;
    }

    public String getLastName() {
        return lastName;
    }

    public String getCity() {
        return city;
    }

    public String getFirstName() {
        return firstName;
    }

    public Integer getId() {
        return id;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}
