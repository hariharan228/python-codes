import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num_of_test_cases = scanner.nextInt();
        List<Integer> prizes = new ArrayList<>();

        while (num_of_test_cases > 0) {
            num_of_test_cases--;
            int num_of_employees = scanner.nextInt();
            int[] employees = new int[num_of_employees];

            for (int i = 0; i < num_of_employees; i++) {
                employees[i] = scanner.nextInt();
            }

            int prizes_sum = 0;
            for (int i = 0; i < num_of_employees; i++) {
                if (i == 0) {
                    if (employees[i] > employees[1]) {
                        prizes_sum += 2;
                    } else {
                        prizes_sum += 1;
                    }
                } else if (i == num_of_employees - 1) {
                    if (employees[num_of_employees - 1] > employees[num_of_employees - 2]) {
                        prizes_sum += 2;
                    } else {
                        prizes_sum += 1;
                    }
                } else {
                    if (employees[i] > employees[i - 1] && employees[i] > employees[i + 1]) {
                        prizes_sum += 2;
                    } else {
                        prizes_sum += 1;
                    }
                }
            }

            prizes.add(prizes_sum);
        }

        for (int i : prizes) {
            System.out.println(i);
        }
    }
}
