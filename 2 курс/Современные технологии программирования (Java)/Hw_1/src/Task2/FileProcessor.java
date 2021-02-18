package Task2;

import java.io.*;

public class FileProcessor {

    private File file;
    private String Name;

    public void FileWriter(String Name)  throws IOException {
        this.file = new File(Name);
        this.file.createNewFile();

        FileWriter writer = new FileWriter(this.file);

        writer.write("101 | Александр | 200 | h\n" +
                "102 | Марк | 30000 | f\n" +
                "103 | Егод | 150 | h\n" +
                "104 | Игорь | 1000 | h\n" +
                "105 | Юрий | 25000 | f\n" +
                "106 | Денис | 300 | h\n" +
                "107 | Евгений | 50000 | f\n");
        writer.flush();
        writer.close();
    }
    public void FileReader(String Name)  throws IOException {
        FileReader reader = new FileReader(this.file);
        char[] a = new char[200];   // Количество символов, которое будем считывать
        reader.read(a);   // Чтение содержимого в массив

        for (char c : a)
            System.out.print(c);   // Вывод символов один за другими
        reader.close();
    }
}
