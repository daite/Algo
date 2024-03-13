# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

import unittest

def reorderLogFiles(logs):
    letters = []
    digits = []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

class TestReorderLogFiles(unittest.TestCase):

    def test_reorderLogFiles(self):
        logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
        expected_output = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
        self.assertEqual(reorderLogFiles(logs), expected_output)

    def test_empty_logs(self):
        logs = []
        expected_output = []
        self.assertEqual(reorderLogFiles(logs), expected_output)

    def test_all_digit_logs(self):
        logs = ["1 2 3", "4 5 6", "7 8 9"]
        expected_output = ["1 2 3", "4 5 6", "7 8 9"]
        self.assertEqual(reorderLogFiles(logs), expected_output)

    def test_all_letter_logs(self):
        logs = ["abc def ghi", "jkl mno pqr", "stu vwx yz"]
        expected_output = ["abc def ghi", "jkl mno pqr", "stu vwx yz"]
        self.assertEqual(reorderLogFiles(logs), expected_output)

    def test_mixed_logs_with_same_content(self):
        logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a8 act zoo"]
        expected_output = ["g1 act car", "a8 act zoo", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
        self.assertEqual(reorderLogFiles(logs), expected_output)

if __name__ == '__main__':
    unittest.main()
