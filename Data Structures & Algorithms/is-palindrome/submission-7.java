class Solution {
    public boolean isPalindrome(String s) {
        List<Character> sentence = new ArrayList<>();
        for (char letter: s.toCharArray()) {
            if (Character.isLetterOrDigit(letter)) {
                sentence.add(Character.toLowerCase(letter));
            }
        }
        return sentence.equals(sentence.reversed());
    }
}
