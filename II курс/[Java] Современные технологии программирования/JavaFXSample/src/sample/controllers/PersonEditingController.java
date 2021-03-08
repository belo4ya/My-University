package sample.controllers;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import sample.modules.Person;
import sample.utils.DateUtil;


public class PersonEditingController {
    @FXML
    private TextField firstNameField;
    @FXML
    private TextField lastNameField;
    @FXML
    private TextField streetField;
    @FXML
    private TextField postalCodeField;
    @FXML
    private TextField cityField;
    @FXML
    private TextField birthdayField;

    private Stage dialogStage;
    private Person person;
    private boolean clicked = false;


    public void setDialogStage(Stage dialogStage){
        this.dialogStage = dialogStage;
    }

    @FXML
    private void initialize() {
    }

    public void setPerson(Person person) {
        this.person = person;
        firstNameField.setText(person.getFirstName());
        lastNameField.setText(person.getLastName());
        streetField.setText(person.getStreet());
        try{
            postalCodeField.setText(Integer.toString(person.getPostalCode()));
        }
        catch(NullPointerException e){
            postalCodeField.setText("");
        }

        postalCodeField.setPromptText("XXXXXX");
        cityField.setText(person.getCity());
        birthdayField.setText(DateUtil.format(person.getBirthDay()));
        birthdayField.setPromptText("dd.mm.yyyy");
    }

    public boolean isClicked() {
        return clicked;
    }

    public boolean isDataValid() {
        String outMessage = "";
        if (firstNameField.getText() == null || firstNameField.getText().length() == 0) {
            outMessage += "No valid first name!\n";
        }
        if (lastNameField.getText() == null || lastNameField.getText().length() == 0) {
            outMessage += "No valid last name!\n";
        }
        if (streetField.getText() == null || streetField.getText().length() == 0) {
            outMessage += "No valid street!\n";
        }
        if (postalCodeField.getText() == null || postalCodeField.getText().length() == 0) {
            outMessage += "No valid postal code!\n";
        }
        if (postalCodeField.getText() == null || postalCodeField.getText().length() == 0) {
            outMessage += "No valid postal code!\n";
        }
        if (cityField.getText() == null || cityField.getText().length() == 0) {
            outMessage += "No valid city!\n";
        }
        if (postalCodeField.getText() == null || postalCodeField.getText().length() == 0) {
            outMessage += "No valid postal code!\n";
        }
        else{
            try {
                Integer.parseInt(postalCodeField.getText());
            } catch (NumberFormatException e) {
                outMessage += "postal code must be an integer!\n";
            }
        }
        if (birthdayField.getText() == null || birthdayField.getText().length() == 0) {
            outMessage += "No valid birthday!\n";
        } else {
            if (!DateUtil.validDate(birthdayField.getText())) {
                outMessage += "Use the format dd.mm.yyyy for datetime!\n";
            }
        }

        if (outMessage.equals("")){
            return true;
        }
        Alert alert = new Alert(AlertType.ERROR);
        alert.initOwner(dialogStage);
        alert.setTitle("Not valid fields!");
        alert.setHeaderText("Please correct invalid fields!");
        alert.setContentText(outMessage);
        alert.showAndWait();
        return false;

    }

    @FXML
    private void handleOkPerson(){
        if(isDataValid()){

            person.setFirstName(firstNameField.getText());
            person.setLastName(lastNameField.getText());
            person.setStreet(streetField.getText());
            person.setPostalCode(Integer.parseInt(postalCodeField.getText()));
            person.setCity(cityField.getText());
            person.setBirthDay(DateUtil.parse(birthdayField.getText()));
            clicked = true;
            dialogStage.close();
        }

    }

    @FXML
    private void handleCancel() {
        dialogStage.close();
    }

}
