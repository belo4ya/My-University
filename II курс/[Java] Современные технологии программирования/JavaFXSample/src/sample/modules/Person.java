package sample.modules;

import javafx.beans.property.*;

import java.time.LocalDate;

public class Person {
    private StringProperty firstName;
    private StringProperty lastName;
    private StringProperty street;
    private StringProperty city;
    private SimpleObjectProperty<Integer> postalCode;
    private ObjectProperty<LocalDate> birthDay;
    public Person(){
        this(null,null,null,null,null,null);
    }

    public Person(String firstName,String lastName, String street,String city,Integer postalCode, LocalDate birthDay){
        this.firstName = new SimpleStringProperty(firstName);
        this.lastName = new SimpleStringProperty(lastName);
        this.street = new SimpleStringProperty(street);
        this.city = new SimpleStringProperty(city);
        this.postalCode = new SimpleObjectProperty<>(postalCode);
        this.birthDay = new SimpleObjectProperty<>(birthDay);
    }
    public String getFirstName() {
        return firstName.get();
    }
    public Integer getPostalCode() {
        return postalCode.get();
    }
    public String getCity() {
        return city.get();
    }
    public String getLastName() {
        return lastName.get();
    }
    public LocalDate getBirthDay() {
        return birthDay.get();
    }
    public String getStreet() {
        return street.get();
    }

    public StringProperty getFirstNameProperty() {
        return firstName;
    }
    public SimpleObjectProperty<Integer> getPostalCodeProperty() {
        return postalCode;
    }
    public StringProperty getCityProperty() {
        return city;
    }
    public StringProperty getLastNameProperty() { return lastName;}
    public ObjectProperty<LocalDate> getBirthDayProperty() { return birthDay; }
    public StringProperty getStreetProperty() { return street;}

    public void setFirstName(String firstName) {
        this.firstName.set(firstName);
    }
    public void setLastName(String lastName) {
        this.lastName.set(lastName);
    }
    public void setBirthDay(LocalDate birthDay) {
        this.birthDay.set(birthDay);
    }
    public void setCity(String city) {
        this.city.set(city);
    }
    public void setPostalCode(int postalCode) {
        this.postalCode.set(postalCode);
    }
    public void setStreet(String street) {
        this.street.set(street);
    }
}
