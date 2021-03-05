package Task_2;

import java.io.File;
import java.io.FileInputStream;
import java.util.Date;

public class Main {

    public static void main(String[] args) {
        Date date = new Date();
        System.out.println(date.toString());
        String D = new String(date.toString());
        System.out.println("C:\Users\anast\Documents\"+D.substring(8, 10)+"_"+D.substring(4, 7)+"_"+D.substring(24, 28));
        File file = new File("C:\Users\anast\Documents\"+D.substring(8, 10)+"_"+D.substring(4, 7)+"_"+D.substring(24, 28));
    }
}
