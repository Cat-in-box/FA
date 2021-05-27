import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Methods {
    private static HashMap<Integer, User> UsersMap = new HashMap<>();

    public Methods(List<User> userList) {
        this.UsersMap = UsersMap;
        for (User user : userList) {
            this.UsersMap.put(user.id, user);
        }
    }

    public List<User> getUsersBySex(Sex sex) {
        List<User> UsersBySexList = new ArrayList<>();
        for (User user : UsersMap.values()) {
            if (user.sex.equals(sex)) {
                UsersBySexList.add(user);
            }
        }

        return UsersBySexList;
    }

    public List<User> getAllUsers() {
        return UsersMap.values().stream().toList();
    }

    public Integer getNumberOfUsers() {
        return UsersMap.size();
    }

    public Integer getNumberOfUsersBySex(Sex sex) {
        return getUsersBySex(sex).size();
    }

    public Integer getAvgAgeOfAllUsers() {
        Integer sumAge = 0;
        for (User user : UsersMap.values()) {
            sumAge += user.age;
        }

        return sumAge/this.getNumberOfUsers();
    }

    public Integer getAvgAgeOfUsersBySex(Sex sex) {
        Integer sumAge = 0;
        Integer counter = 0;
        for (User user : UsersMap.values()) {
            if (user.sex.equals(sex)) {
                sumAge += user.age;
                counter += 1;
            }
        }

        return sumAge/counter;
    }

    public boolean equals(User user1, User user2) {
        if (user1.name.equals(user2.name) && user1.age.equals(user2.age) && user1.sex.equals(user2.sex)) {
            return true;
        }
        return false;
    }

}
