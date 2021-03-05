package Task1;

class Listener implements StringBuilderListener {

    public void Changed(StringBuilderWr StringBuilder) {
        System.out.println("Строка обновлена: " + StringBuilder.toString());
    }
}
