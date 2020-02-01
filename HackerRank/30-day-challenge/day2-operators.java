/* https://www.hackerrank.com/challenges/30-operators/problem */
public class Solution {

    static void solve(double meal_cost, int tip_percent, int tax_percent) {

        int totalCost = (int) Math.round(meal_cost + (meal_cost * tip_percent * 0.01) + (meal_cost * tax_percent * 0.01));
        System.out.println( totalCost );
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        double meal_cost = scanner.nextDouble();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int tip_percent = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int tax_percent = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        solve(meal_cost, tip_percent, tax_percent);

        scanner.close();
    }
}