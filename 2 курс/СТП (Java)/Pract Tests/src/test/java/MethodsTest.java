import org.junit.After;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

public class MethodsTest {

    private User user1 = new User(1, "Евгений", 35, Sex.MALE);
    private User user2 = new User(2, "Мария", 41, Sex.FEMALE);
    private User user3 = new User(3, "Петр", 12, Sex.MALE);
    private User user4 = new User(4, "Мария", 41, Sex.FEMALE);
    private Methods UserMethods = new Methods(List.of(user1, user2, user3, user4));

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void getUsersBySex() {
        List<User> expected = UserMethods.getUsersBySex(Sex.MALE);

        List<User> actual = new ArrayList<>();
        actual.add(user1);
        actual.add(user3);

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void getAllUsers() {
        List<User> expected = UserMethods.getAllUsers();

        List<User> actual = new ArrayList<>();
        actual.add(user1);
        actual.add(user2);
        actual.add(user3);
        actual.add(user4);

        Assert.assertEquals(expected, actual);

    }

    @Test
    public void getNumberOfUsers() {
        Integer expected = UserMethods.getNumberOfUsers();
        Integer actual = 4;

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void getNumberOfUsersBySex() {
        Integer expected = UserMethods.getNumberOfUsersBySex(Sex.MALE);
        Integer actual = 2;

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void getAvgAgeOfAllUsers() {
        Integer expected = UserMethods.getAvgAgeOfAllUsers();
        Integer actual = (user1.age + user2.age + user3.age + user4.age)/4;

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void getAvgAgeOfUsersBySex() {
        Integer expected = UserMethods.getAvgAgeOfUsersBySex(Sex.MALE);
        Integer actual = (user1.age + user3.age)/2;

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void equals() {
        boolean expected = UserMethods.equals(user2, user4);
        boolean actual = true;

        Assert.assertEquals(expected, actual);
    }
}