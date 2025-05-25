/**
 * @param {string} s
 * @return {number}
 */
var maxFreqSum = function(s) {
    const freq = {};
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let maxVowel = 0;
    let maxConsonant = 0;

    
    for (let char of s.toLowerCase()) {
        if (/[a-z]/.test(char)) { 
            freq[char] = (freq[char] || 0) + 1;
        }
    }

    
    for (let char in freq) {
        if (vowels.has(char)) {
            maxVowel = Math.max(maxVowel, freq[char]);
        } else {
            maxConsonant = Math.max(maxConsonant, freq[char]);
        }
    }

    return maxVowel + maxConsonant;
};