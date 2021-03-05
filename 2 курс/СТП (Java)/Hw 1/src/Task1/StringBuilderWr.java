package Task1;

public class StringBuilderWr {

    private StringBuilderListener Listener; // слушатель
    private StringBuilder StringBuilder; // делегат

    public StringBuilderWr() {
        StringBuilder = new StringBuilder();
    }

    public void setChangeListener(StringBuilderListener Listener) {
        this.Listener = Listener;
    }

    private void notifyListener(){
        if (Listener != null) {
            Listener.Changed(this);
        }
    }

    public StringBuilderWr append(Object obj) {
        StringBuilder.append(obj);
        notifyListener();
        return this;
    }

    public StringBuilderWr replace(int start, int end, String str) {
        StringBuilder.replace(start, end, str);
        notifyListener();
        return this;
    }

    public StringBuilderWr insert(int index, char[] str, int offset, int len) {
        StringBuilder.insert(index, str, offset, len);
        notifyListener();
        return this;
    }

    // Другие методы

    public String toString() {
        return StringBuilder.toString();
    }
}