package Task_4;

import java.util.ArrayList;
import java.util.Scanner;

public class Student implements  setPerson {

    ArrayList <String> student;
    Scanner scanner;

    public Student() {
        this.student = new ArrayList<String>();
        scanner = new Scanner(System.in);
    }


    public ArrayList setName() {
        while (true) {
            System.out.println("Input student name ");
            String s = scanner.next();
            if (s.equals("break")) {
                break;
            } else {
                student.add(s);
            }
        }
        return student;
    }

    public String getName() {
        return null;
    }

    public String setAge(String ... student) {
        String students = null;
        if (student.length==2) {
            student[0] = "23";
            student[1] = "33";
        }
        students = student[0] + " " + student[1];
        return students;
    }
}
