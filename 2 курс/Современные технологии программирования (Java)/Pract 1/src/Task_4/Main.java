package Task_4;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList <String> person = new ArrayList<String>();
        person.add("Иван");
        person.add("Петр");
        person.add("Юля");

        System.out.println("Персона " + person.get(0));
        System.out.println(person.toString());
        person.remove("Иван");
        System.out.println(person.toString());

        Student student = new Student();
        person = student.setName();
        System.out.println(person.toString());
        System.out.println(student.setAge("n", "m"));
    }
}
