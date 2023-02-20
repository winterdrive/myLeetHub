class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        String tempWord = "";
        for (int i = 0; i<dictionary.size(); i++) {
            String word=dictionary.get(i);
            if (isSubString(word, s)) {
                if ((word.length() == tempWord.length() && word.compareTo(tempWord) < 0)
                        || word.length() > tempWord.length()) {
                    tempWord = word;
                }
            }
        }
        return tempWord;
    }
    
    
    private static boolean isSubString(String word, String s) {
        int i = 0, j = 0;
        while (i< word.length() && j < s.length()) {
            if (word.charAt(i) == s.charAt(j)) {
                i++;
            }
            j++;
        }
        return i == word.length();
    }
    
}