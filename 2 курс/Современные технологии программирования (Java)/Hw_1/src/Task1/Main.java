package Task1;

public class Main {

    public static void main(String[] args) {
        StringBuilderWr NewSB = new StringBuilderWr();
        NewSB.setChangeListener(new Listener());
        NewSB.append("Meow");
        NewSB.append("! ");
        NewSB.append("Purrr");
    }
}
