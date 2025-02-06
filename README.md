# WhitedCrypt

**FYI: Because I moved this repository from my old account to this one, my old commits appear as from my old account.**

An encryption algorithm I developed to experiment with simple encryption algorithms. I think there's no need to mention this, but the algorithm can't be considered secure enough and **I DO NOT RECOMMEND using this algorithm for encrypting anything sensitive**.
If any data you encrypt using this algorithm gets cracked, the responsibility of that is fully on you.

## How does it work?
To put it simply, there are 4 functions:

**Encode(*MaskingMethod: int*, *PlainText: str*):**
- Goes over each character in [PlainText].
- Gets the Unicode character of the current character.
- Creates a [UnicodeGroup] (Where all the unicode numbers are in one string) with separators (e.g. "unicode1\unicode2\unicode3").
- Loops over each unicode in the [UnicodeGroup].
- Masks the [UnicodeGroup] by replacing each unicode character with different characters according to the currently selected masking method.

**Decode(*EncodedText: str*):**
- Does the opposite of [Encode].

**Encrypt(*HashingAlgorithmName: str*, *PlainText: str*, *Key: str*):**
- Hashes the [Key] with the currently selected hashing algorithm.
- Encodes the [HashedKey] using the [Encode] function with number masking.
- Also encodes the [PlainText] using the [Encode] function with number masking.
* The reason we're using number masking here is to convert these strings into logical numbers which we can then do mathematical operations on.
* Now that both [HashedKey] and [PlainText] are logical numbers, we can do mathematical operations on them.
- Adds [EncodedHashedKey] to [EncodedPlainText].
* When I say adds, I don't mean it appends it to the end of the string, it literally adds them as a mathematical operation, which means to get the [PlainText] back, you need to subtract exactly the [EncodedHashedKey] from the result. Which in turn requires you to have the [Key].
- Lastly, encodes the result with the [Encode] function with the preferred masking type.

**Decrypt(*EncryptedText: str*, *Key: str*):**
- Does the opposite of [Encrypt].
