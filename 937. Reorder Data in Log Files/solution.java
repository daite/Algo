class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letterList = new ArrayList<>();
        List<String> digitList = new ArrayList<>();

        for(String log: logs) {
            if (Character.isDigit(log.split(" ")[1].charAt(0))) {
                digitList.add(log);
            }else {
                letterList.add(log);
            }
        }
        letterList.sort((s1, s2) -> {
            String[] s1x = s1.split(" ", 2);
            String[] s2x = s2.split(" ", 2);

            int compared = s1x[1].compareTo(s2x[1]);
            if (compared == 0 ){
                return s1x[0].compareTo(s2x[0]);
            } else {
                return compared;
            }
        });
        letterList.addAll(digitList);
        return letterList.toArray(new String[0]);
    }
}

// import org.junit.Test;
// import static org.junit.Assert.assertArrayEquals;

// public class SolutionTest {
//     @Test
//     public void testReorderLogFiles() {
//         Solution solution = new Solution();
//         String[] logs = {
//             "a1 9 2 3 1",
//             "g1 act car",
//             "zo4 4 7",
//             "ab1 off key dog",
//             "a8 act zoo"
//         };
//         String[] expectedOutput = {
//             "g1 act car",
//             "a8 act zoo",
//             "ab1 off key dog",
//             "a1 9 2 3 1",
//             "zo4 4 7"
//         };
//         String[] result = solution.reorderLogFiles(logs);
//         assertArrayEquals(expectedOutput, result);
//     }
// }
