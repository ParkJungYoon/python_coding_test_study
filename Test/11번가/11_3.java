package com.codility.tasks.hibernate.solution;

import org.springframework.stereotype.Service;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.beans.factory.annotation.Autowired;

import javax.persistence.Entity;
import javax.persistence.EntityManager;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.List;

import javax.persistence.Column;

@Entity
@Table(name = "person_data")
class Person {

    private String ;
    private String lastName;

    public Person() {

    }

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    @Column(name="first_name", nullable = false)
    public String getFirstName() {
        return firstName;
    }
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    @Column(name="last_name", nullable = false)
    public String getFirstName() {
        return lastName;
    }
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    @Override
    public String getFullName() {
        return firstName + lastName;
    }
}

public interface UserRepository extends JpaRepository<Person, Long> {
    List<Person> findAll();
}


@Service
class PersonService {
    @Autowired
    private UserRepository userRepository;

    @Override
    List<Person> findAll() {
        return userRepository.findAll();
    }

}
