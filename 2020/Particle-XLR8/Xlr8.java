import java.util.Scanner;

class Xlr8 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int distance = sc.nextInt();
        if ((distance - 5) % 8 == 1) {
            System.out.println(1);
        } else if ((distance - 5) % 8 == 2) {
            System.out.println(2);
        } else if ((distance - 5) % 8 == 3) {
            System.out.println(3);
        }
    }
}